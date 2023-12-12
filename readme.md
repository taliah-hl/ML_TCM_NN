# NN Model for TCM Project (Group 13)

## 12/12 新方向
1. 睇f1 高分的藥有什麼特徵 -> e.g. 0 & 1比例
2. 比較TP, FP, TN,FN of train set and val set
3. 用xx 湯去train?
4. reduce dimension of X (feature)??? 


### print accuracy and loss tutorial
https://machinelearningmastery.com/display-deep-learning-model-training-history-in-keras/

## fisrt runnable version with super simplified data

`cnn_simplfied_data1.ipynb`

## train one medicine each time
`one_medicine_vX.ipynb`
- v1: train 所有藥
- v2: 只train 出現次數多於250 的藥 (=剛好剩10種藥)
- v3: v2 加入compute_sample_weight


## train all medicine at one time 
`multi_classifer_vX.ipynb`

- 未完成!!!

### Cheat sheet

| var | description|
|---|---|
| `df_predictions`  | probability of "has" that medicine (有該藥材)  |
| `all_class_binary_prediction_df`  | predicted as 是否有該藥材  |
|  `val_y` | ground truth of 是否有該藥材  |
|   |   |

`df_predictions` =  probability of "has" that medicine (有該藥材)

`all_class_binary_prediction_df` = predicted as 是否有該藥材

`val_y` = ground truth of 是否有該藥材

## install packages
run
```
pip install -r requirements.txt
# if use conda
conda install --yes --file requirements.txt
```
.

.

.

.


.

.

## sample code (顯示tensorflow.keras 的NN model 怎麼用)

`try_nn_1.ipynb`


## 例子

CNN 辦識手寫文字例子
https://medium.com/jameslearningnote/%E8%B3%87%E6%96%99%E5%88%86%E6%9E%90-%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92-%E7%AC%AC5-1%E8%AC%9B-%E5%8D%B7%E7%A9%8D%E7%A5%9E%E7%B6%93%E7%B6%B2%E7%B5%A1%E4%BB%8B%E7%B4%B9-convolutional-neural-network-4f8249d65d4f

