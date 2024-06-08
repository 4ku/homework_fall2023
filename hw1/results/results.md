Here is a clean and structured markdown report for your experiments:

# Behavioral Cloning

## Best Hyperparameters

The first row - is an expert score.  

### Hopper-v4
|   Rank |   Eval_AverageReturn |   learning_rate |   n_layers |   num_agent_train_steps_per_iter |   size |   train_batch_size |
|-------:|---------------------:|----------------:|-----------:|---------------------------------:|-------:|-------------------:|
|      0 |              3717.51 |         nan     |        nan |                              nan |    nan |                nan |
|      1 |              3708.83 |           0.005 |          2 |                            10000 |     16 |               1000 |
|      2 |              3653.88 |           0.01  |          2 |                            10000 |     16 |               1000 |
|      3 |              3518.8  |           0.005 |          1 |                            10000 |     64 |               1000 |
|      4 |              3436.38 |           0.005 |          2 |                            10000 |     64 |               1000 |
|      5 |              3363.43 |           0.01  |          2 |                            10000 |     32 |               1000 |
|      6 |              3253.96 |           0.005 |          4 |                            10000 |     32 |               1000 |
|      7 |              3249.88 |           0.01  |          1 |                            10000 |     32 |                100 |
|      8 |              3152.92 |           0.01  |          4 |                            10000 |     32 |               1000 |
|      9 |              2895.97 |           0.005 |          2 |                            10000 |    128 |               1000 |
|     10 |              2874.33 |           0.005 |          1 |                            10000 |     32 |               1000 |

### Ant-v4
|   Rank |   Eval_AverageReturn |   learning_rate |   n_layers |   num_agent_train_steps_per_iter |   size |   train_batch_size |
|-------:|---------------------:|----------------:|-----------:|---------------------------------:|-------:|-------------------:|
|      0 |              4681.89 |         nan     |        nan |                              nan |    nan |                nan |
|      1 |              4793.67 |           0.01  |          2 |                             5000 |     64 |                100 |
|      2 |              4765.21 |           0.01  |          2 |                             5000 |    128 |                500 |
|      3 |              4756.07 |           0.005 |          2 |                             5000 |    128 |                500 |
|      4 |              4749.49 |           0.005 |          2 |                             5000 |     32 |               1000 |
|      5 |              4727.12 |           0.01  |          2 |                             5000 |     64 |               1000 |
|      6 |              4724.18 |           0.005 |          2 |                             5000 |    128 |               1000 |
|      7 |              4722.7  |           0.01  |          2 |                             5000 |     32 |               1000 |
|      8 |              4722.02 |           0.01  |          4 |                             5000 |     64 |               1000 |
|      9 |              4716.25 |           0.005 |          4 |                             5000 |    128 |               1000 |
|     10 |              4711.91 |           0.005 |          2 |                             5000 |     64 |               1000 |

### Walker2d-v4
|   Rank |   Eval_AverageReturn |   learning_rate |   n_layers |   num_agent_train_steps_per_iter |   size |   train_batch_size |
|-------:|---------------------:|----------------:|-----------:|---------------------------------:|-------:|-------------------:|
|      0 |              5383.31 |         nan     |        nan |                              nan |    nan |                nan |
|      1 |              5367.07 |           0.005 |          2 |                             5000 |     64 |                500 |
|      2 |              5258.18 |           0.01  |          2 |                             5000 |     64 |                500 |
|      3 |              5059.8  |           0.01  |          2 |                             5000 |    128 |                500 |
|      4 |              4413.9  |           0.005 |          4 |                             5000 |     64 |                500 |
|      5 |              4331.6  |           0.005 |          2 |                             5000 |     64 |                100 |
|      6 |              4290.77 |           0.005 |          4 |                             5000 |    128 |                500 |
|      7 |              4114.14 |           0.005 |          2 |                            10000 |     64 |                100 |
|      8 |              3351.94 |           0.005 |          8 |                             5000 |     64 |                500 |
|      9 |              3043.74 |           0.001 |          2 |                             5000 |     64 |                500 |
|     10 |              2705.09 |           0.01  |          4 |                             5000 |     64 |                500 |

### HalfCheetah-v4
|   Rank |   Eval_AverageReturn |   learning_rate |   n_layers |   num_agent_train_steps_per_iter |   size |   train_batch_size |
|-------:|---------------------:|----------------:|-----------:|---------------------------------:|-------:|-------------------:|
|      0 |              4034.8  |         nan     |        nan |                              nan |    nan |                nan |
|      1 |              4131.43 |           0.005 |          2 |                            10000 |     64 |                100 |
|      2 |              4079.83 |           0.005 |          4 |                             5000 |    128 |                500 |
|      3 |              4077.75 |           0.01  |          2 |                             5000 |    128 |                500 |
|      4 |              4075.57 |           0.005 |          4 |                             5000 |    256 |                500 |
|      5 |              4066.28 |           0.01  |          2 |                             5000 |     64 |                500 |
|      6 |              4048.08 |           0.005 |          4 |                             5000 |     64 |                500 |
|      7 |              4038.26 |           0.01  |          8 |                             5000 |     64 |                500 |
|      8 |              4033.32 |           0.01  |          4 |                             5000 |     64 |                500 |
|      9 |              4032.38 |           0.005 |          8 |                             5000 |     64 |                500 |
|     10 |              4020.6  |           0.01  |          8 |                             5000 |    128 |                500 |

## Compare Hyperparameters

The default parameters used in the experiments are set to provide a baseline for comparison. These default settings are:

- **Number of Layers:** 2
- **Size:** 64
- **Learning Rate:** 0.005
- **Number of Agent Training Steps per Iteration:** 1000
- **Training Batch Size:** 100

To understand the impact of different hyperparameters on the performance of the models, we varied each of these parameters within specified ranges. The values searched for each hyperparameter are:

- **Number of Layers:** 1, 2, 4, 8
- **Size:** 16, 32, 64, 128, 256
- **Learning Rate:** 0.0001, 0.0005, 0.001, 0.005, 0.01
- **Number of Agent Training Steps per Iteration:** 100, 1000, 5000, 10000
- **Training Batch Size:** 1, 10, 100, 1000

### Hopper-v4
The plot below shows the comparison of the different hyperparameters on the Hopper-v4 environment. Each subplot represents the impact of varying one specific hyperparameter while keeping the others at their default values.

**Plot with Comparisons:**
![Hopper-v4 Comparison](plots/bc_hopper/combined_plots.png)

### Ant-v4
Similarly, the plot for the Ant-v4 environment illustrates how different settings of the hyperparameters affect the performance. This helps in identifying the most effective configurations for training.

**Plot with Comparisons:**
![Ant-v4 Comparison](plots/bc_ant/combined_plots.png)

### Walker2d-v4
For the Walker2d-v4 environment, the plot provides insights into which hyperparameters contribute most significantly to the model's success and can guide future tuning efforts.

**Plot with Comparisons:**
![Walker2d-v4 Comparison](plots/bc_walker/combined_plots.png)

### HalfCheetah-v4
The HalfCheetah-v4 environment's plot demonstrates the influence of each hyperparameter on the model's performance, aiding in the selection of optimal values for better results.

**Plot with Comparisons:**
![HalfCheetah-v4 Comparison](plots/bc_halfcheetah/combined_plots.png)

# DAgger

