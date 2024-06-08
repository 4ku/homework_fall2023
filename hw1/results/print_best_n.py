import glob
import pandas as pd
from tbparse import SummaryReader

def get_hparams(log_dir):
    reader = SummaryReader(log_dir)
    return reader.hparams

def get_eval_average_return(log_dir):
    reader = SummaryReader(log_dir)
    df = reader.scalars
    if "tag" in df:
        eval_return = df[df['tag'] == 'Eval_AverageReturn']
        eval_std_return = df[df['tag'] == 'Eval_StdReturn']  # Uncomment this line
        if not eval_return.empty:
            eval_avg = eval_return['value'].iloc[-1]
            eval_std = eval_std_return['value'].iloc[-1] if not eval_std_return.empty else None
            return eval_avg, eval_std  # Return both values
    return None, None

def get_train_average_return(log_dir):
    reader = SummaryReader(log_dir)
    df = reader.scalars
    if "tag" in df:
        train_return = df[df['tag'] == 'Train_AverageReturn']
        train_std_return = df[df['tag'] == 'Train_StdReturn']  # Uncomment this line
        if not train_return.empty:
            train_avg = train_return['value'].max()
            train_std = train_std_return['value'].max() if not train_std_return.empty else None
            return train_avg, train_std  # Return both values
    return None, None

def main():
    # exp_name = "dagger_ant"
    # exp_name = "bc_ant"
    exp_name = "dagger_hopper"
    # exp_name = "bc_hopper"
    log_dirs = glob.glob(f'../data/{exp_name}/*')

    results = []
    train_average_return = None
    train_std_return = None
    for log_dir in log_dirs:
        eval_return, eval_std = get_eval_average_return(log_dir)
        train_return, train_std = get_train_average_return(log_dir)
        if train_return is not None:
            if train_average_return is None or train_return > train_average_return:
                train_average_return = train_return
                train_std_return = train_std
        if eval_return is not None:
            hparams = get_hparams(log_dir)
            results.append((eval_return, eval_std, hparams, log_dir))

    # Sort results by Eval_AverageReturn in descending order
    results.sort(reverse=True, key=lambda x: x[0])

    # Hyperparameters to print
    target_hparams = {"n_layers", "size", "learning_rate", "num_agent_train_steps_per_iter", "train_batch_size"}

    # Collect data for table
    table_data = []
    # Add zero row for Train_AverageReturn
    if train_average_return is not None and exp_name.startswith("bc"):
        zero_row = {"Eval_AverageReturn": train_average_return, "Eval_StdReturn": train_std_return}
        table_data.append(zero_row)

    for i, (eval_return, eval_std, hparams, log_dir) in enumerate(results):
        row = {"Eval_AverageReturn": eval_return, "Eval_StdReturn": eval_std}
        if not hparams.empty:
            for _, param in hparams.iterrows():
                if param['tag'] in target_hparams:
                    row[param['tag']] = param['value']
        table_data.append(row)

    # Create DataFrame and remove duplicates
    df = pd.DataFrame(table_data)
    df = df.drop_duplicates(subset=["Eval_AverageReturn", "Eval_StdReturn", *target_hparams], keep='first')

    # Keep only the first 10 unique rows
    df = df.head(10)

    print(df)

    # Save DataFrame to a markdown file
    with open(f'results_table_{exp_name}.md', 'w') as f:
        f.write(df.to_markdown(index=False))

if __name__ == "__main__":
    main()
