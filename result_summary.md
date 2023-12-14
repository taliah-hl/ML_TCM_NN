# Result 比較

# Train all X, y

## 100 epoch 
- model layer: 16-32-32-2, epoch=100, batch_size=32,  activation=relu, num_med:all, del_med_under_thres=0
- val set:
```
'overall': {
        'TP': 418,
        'FP': 383,
        'FN': 1472,
        'TN': 13945,
        'TP_percentage': {
            0.025773831545196694
        },
        'FP_percentage': {
            0.023615735602417066
        },
        'FN_percentage': {
            0.0907633493649032
        },
        'TN_percentage': {
            0.8598470834874831
        },
        'f1_score': 0.31066518023039763,
        'mean_accuracy': 0.8856209150326797,
        'precision': 0.5218476903870163,
        'recall': 0.22116402116402117
    }
```

- train set:
  - train set model layer: 16 - 32 - 32 - 2, epoch = 100, batch_size = 32, activation = relu, num_med: all, del_med_under_thres = 0
  ```
   {
    'TP': 2230,
    'FP': 1070,
    'FN': 4754,
    'TN': 56920,
    'TP_percentage': 0.03432142087604272,
    'FP_percentage': 0.01646812571182319,
    'FN_percentage': 0.0731677286299135,
    'TN_percentage': 0.8760427247822206,
    'overall_f1': 0.43368339167639053,
    'precision': 0.6757575757575758,
    'recall': 0.3193012600229095
  }
  ```
  
 


## 1000 epoch

- model layer: 32 - 64 - 128 - 64 - 32 units, activation: relu, optimizer: Adam, learning rate: 0.001, epochs: 1000, batch_size: 32, num_med: all.del_med_under_thres: 0
- val set:
    ```
     'overall': {
        'TP': 479,
        'FP': 592,
        'FN': 1411,
        'TN': 13736,
        'TP_percentage': {
            0.029535084474041188
        },
        'FP_percentage': {
            0.03650265137501541
        },
        'FN_percentage': {
            0.0870020964360587
        },
        'TN_percentage': {
            0.8469601677148847
        },
        'f1_score': 0.32353934481594054,
        'mean_accuracy': 0.8764952521889259,
        'precision': 0.44724556489262374,
        'recall': 0.25343915343915346
    }
    ```

- train set:
```
{
    'TP': 3154,
    'FP': 1015,
    'FN': 3830,
    'TN': 56975,
    'TP_percentage': 0.048542493920645184,
    'FP_percentage': 0.015621633268692092,
    'FN_percentage': 0.05894665558531105,
    'TN_percentage': 0.8768892172253516,
    'overall_f1': 0.565587734241908,
    'precision': 0.7565363396497962,
    'recall': 0.4516036655211913
}
```
