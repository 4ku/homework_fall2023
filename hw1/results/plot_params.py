import glob
import os
import matplotlib.pyplot as plt
from tbparse import SummaryReader
import numpy as np

# Define default parameters
# DEFAULT_PARAMS = {
#     "n_layers": 2,
#     "size": 64,
#     "learning_rate": 5e-3,
#     "num_agent_train_steps_per_iter": 1000,
#     "train_batch_size": 100
# }

DAGGER_DEFAULT_PARAMS = {
    "n_layers": 2,
    "size": 64,
    "learning_rate": 5e-3,
    "num_agent_train_steps_per_iter": 1000,
    "train_batch_size": 300
}

def get_hparams(log_dir):
    reader = SummaryReader(log_dir)
    return reader.hparams

def get_eval_returns(log_dir):
    reader = SummaryReader(log_dir)
    df = reader.scalars
    if "tag" in df:
        eval_return = df[df['tag'] == 'Eval_AverageReturn']
        eval_std_return = df[df['tag'] == 'Eval_StdReturn']
        if not eval_return.empty and not eval_std_return.empty:
            # Return the last logged value for both average and std return
            return eval_return['value'].iloc[-1], eval_std_return['value'].iloc[-1]
    return None, None

def get_train_average_return(log_dir):
    reader = SummaryReader(log_dir)
    df = reader.scalars
    if "tag" in df:
        train_return = df[df['tag'] == 'Train_AverageReturn']
        if not train_return.empty:
            # Return the maximum logged value
            return train_return['value'].max()
    return None

def get_experiments_data(log_dirs):
    results = []
    train_average_return = None
    for log_dir in log_dirs:
        eval_return, eval_std_return = get_eval_returns(log_dir)
        if eval_return is not None:
            hparams = get_hparams(log_dir)
            results.append((eval_return, eval_std_return, hparams, log_dir))
        train_return = get_train_average_return(log_dir)
        if train_return is not None:
            if train_average_return is None or train_return > train_average_return:
                train_average_return = train_return
    return results, train_average_return

def filter_results(results, param_name, default_params):
    filtered = []
    for eval_return, eval_std_return, hparams, log_dir in results:
        all_defaults_match = all(hparams[hparams['tag'] == k]['value'].values[0] == v for k, v in default_params.items() if k != param_name)
        if all_defaults_match:
            value = hparams[hparams['tag'] == param_name]['value'].values[0]
            filtered.append((value, eval_return, eval_std_return))
    return filtered

def plot_individual(param_name, results, default_params, train_average_return, exp_name):
    filtered_results = filter_results(results, param_name, default_params)
    filtered_results.sort()

    # Group results by the parameter value
    grouped_results = {}
    for value, eval_return, eval_std_return in filtered_results:
        if value not in grouped_results:
            grouped_results[value] = []
        grouped_results[value].append((eval_return, eval_std_return))
    
    values = list(grouped_results.keys())
    means = []
    std_devs = []

    for value in values:
        returns = [result[0] for result in grouped_results[value]]
        stds = [result[1] for result in grouped_results[value]]
        mean_return = np.mean(returns)
        mean_std = np.mean(stds)
        means.append(mean_return)
        std_devs.append(mean_std)

    values = [str(key) for key in list(grouped_results.keys())]
    plt.figure()
    plt.errorbar(values, means, yerr=std_devs, fmt='o', capsize=5)
    plt.axhline(y=train_average_return, color='r', linestyle='--', label='Train_AverageReturn')
    plt.xlabel(param_name)
    plt.ylabel('Eval_AverageReturn')
    plt.title(f'{exp_name}')
    plt.legend()
    plt.grid(True)

    # Ensure the plots directory exists
    plots_dir = f'plots/{exp_name}'
    os.makedirs(plots_dir, exist_ok=True)
    plt.savefig(f'{plots_dir}/plot_{param_name}.png')

def plot_combined(param_name, results, default_params, train_average_return, exp_name, ax):
    filtered_results = filter_results(results, param_name, default_params)
    filtered_results.sort()

    # Group results by the parameter value
    grouped_results = {}
    for value, eval_return, eval_std_return in filtered_results:
        if value not in grouped_results:
            grouped_results[value] = []
        grouped_results[value].append((eval_return, eval_std_return))
    
    values = list(grouped_results.keys())
    means = []
    std_devs = []

    for value in values:
        returns = [result[0] for result in grouped_results[value]]
        stds = [result[1] for result in grouped_results[value]]
        mean_return = np.mean(returns)
        mean_std = np.mean(stds)
        means.append(mean_return)
        std_devs.append(mean_std)

    values = [str(key) for key in list(grouped_results.keys())]
    ax.errorbar(values, means, yerr=std_devs, fmt='o', capsize=5)
    ax.axhline(y=train_average_return, color='r', linestyle='--', label='Train_AverageReturn')
    ax.set_xlabel(param_name)
    ax.set_ylabel('Eval_AverageReturn')
    ax.set_title(f'{exp_name}')
    ax.legend()
    ax.grid(True)

def main():
    # exp_name = "bc_walker"
    exp_name = "dagger_ant"
    log_dirs = glob.glob(f'../data/{exp_name}/*')

    results, train_average_return = get_experiments_data(log_dirs)

    # Hyperparameters to plot
    params_to_plot = ["n_layers", "size", "learning_rate", "num_agent_train_steps_per_iter", "train_batch_size"]

    # Create separate plots
    for param in params_to_plot:
        plot_individual(param, results, DAGGER_DEFAULT_PARAMS, train_average_return, exp_name)

    # Create combined plot in a 3x2 grid
    fig, axes = plt.subplots(3, 2, figsize=(15, 10))
    axes = axes.flatten()

    for ax, param in zip(axes, params_to_plot):
        plot_combined(param, results, DAGGER_DEFAULT_PARAMS, train_average_return, exp_name, ax)

    fig.delaxes(axes[-1])  # Remove the last empty subplot if the number of params is less than the grid size
    plt.tight_layout()

    # Ensure the plots directory exists
    plots_dir = f'plots/{exp_name}'
    os.makedirs(plots_dir, exist_ok=True)
    plt.savefig(f'{plots_dir}/combined_plots.png')

if __name__ == "__main__":
    main()
