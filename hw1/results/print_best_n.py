import glob
import pandas as pd
from tbparse import SummaryReader
from tabulate import tabulate

def get_hparams(log_dir):
    reader = SummaryReader(log_dir)
    return reader.hparams

def get_eval_average_return(log_dir):
    reader = SummaryReader(log_dir)
    df = reader.scalars
    if "tag" in df:
        eval_return = df[df['tag'] == 'Eval_AverageReturn']
        if not eval_return.empty:
            # Return the last logged value
            return eval_return['value'].iloc[-1]
    return None

def get_train_average_return(log_dir):
    reader = SummaryReader(log_dir)
    df = reader.scalars
    if "tag" in df:
        train_return = df[df['tag'] == 'Train_AverageReturn']
        if not train_return.empty:
            # Return the maximum logged value
            return train_return['value'].max()
    return None

def main():
    exp_name = "bc_halfcheetah"
    log_dirs = glob.glob(f'../data/{exp_name}/*')

    results = []
    train_average_return = None
    for log_dir in log_dirs:
        eval_return = get_eval_average_return(log_dir)
        train_return = get_train_average_return(log_dir)
        if train_return is not None:
            if train_average_return is None or train_return > train_average_return:
                train_average_return = train_return
        if eval_return is not None:
            hparams = get_hparams(log_dir)
            results.append((eval_return, hparams, log_dir))

    # Sort results by Eval_AverageReturn in descending order
    results.sort(reverse=True, key=lambda x: x[0])

    # Hyperparameters to print
    target_hparams = {"n_layers", "size", "learning_rate", "num_agent_train_steps_per_iter", "train_batch_size"}

    # Collect data for table
    table_data = []
    # Add zero row for Train_AverageReturn
    if train_average_return is not None and exp_name.startswith("bc"):
        zero_row = {"Rank": 0, "Eval_AverageReturn": train_average_return}
        table_data.append(zero_row)

    for i, (eval_return, hparams, log_dir) in enumerate(results[:10]):
        row = {"Rank": i + 1, "Eval_AverageReturn": eval_return}
        if not hparams.empty:
            for _, param in hparams.iterrows():
                if param['tag'] in target_hparams:
                    row[param['tag']] = param['value']
        table_data.append(row)

    # Create DataFrame and print
    df = pd.DataFrame(table_data)
    print(df)

    # Save DataFrame to a markdown file
    with open(f'results_table_{exp_name}.md', 'w') as f:
        f.write(df.to_markdown(index=False))

if __name__ == "__main__":
    main()
