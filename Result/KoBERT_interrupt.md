## colab에서 interrupt난 버전의 log 

```
2021-04-10 06:22:09.263042: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
=== Argument Setting ===
src: community
tgt: news
seed: 42
train_seed: 42
model_type: bert
max_seq_length: 128
batch_size: 64
pre_epochs: 3
num_epochs: 3
AD weight: 1.0
KD weight: 1.0
temperature: 20
Downloading: 100% 77.8k/77.8k [00:00<00:00, 3.09MB/s]
Downloading: 100% 51.0/51.0 [00:00<00:00, 34.5kB/s]
=== Processing datasets ===
writing example 200 of 1600
writing example 400 of 1600
writing example 600 of 1600
writing example 800 of 1600
writing example 1000 of 1600
writing example 1200 of 1600
writing example 1400 of 1600
writing example 1600 of 1600
writing example 200 of 400
writing example 400 of 400
writing example 200 of 2000
writing example 400 of 2000
writing example 600 of 2000
writing example 800 of 2000
writing example 1000 of 2000
writing example 1200 of 2000
writing example 1400 of 2000
writing example 1600 of 2000
writing example 1800 of 2000
writing example 2000 of 2000
writing example 200 of 1600
writing example 400 of 1600
writing example 600 of 1600
writing example 800 of 1600
writing example 1000 of 1600
writing example 1200 of 1600
writing example 1400 of 1600
writing example 1600 of 1600
Downloading: 100% 426/426 [00:00<00:00, 318kB/s]
Downloading: 100% 369M/369M [00:08<00:00, 43.7MB/s]
=== Training classifier for source domain ===
Epoch [01/03] Step [001/025]: cls_loss=0.6931
Epoch [01/03] Step [002/025]: cls_loss=0.7009
Epoch [01/03] Step [003/025]: cls_loss=0.6580
Epoch [01/03] Step [004/025]: cls_loss=0.6706
Epoch [01/03] Step [005/025]: cls_loss=0.6330
Epoch [01/03] Step [006/025]: cls_loss=0.7246
Epoch [01/03] Step [007/025]: cls_loss=0.7076
Epoch [01/03] Step [008/025]: cls_loss=0.6769
Epoch [01/03] Step [009/025]: cls_loss=0.6862
Epoch [01/03] Step [010/025]: cls_loss=0.7062
Epoch [01/03] Step [011/025]: cls_loss=0.7272
Epoch [01/03] Step [012/025]: cls_loss=0.7063
Epoch [01/03] Step [013/025]: cls_loss=0.6709
Epoch [01/03] Step [014/025]: cls_loss=0.6695
Epoch [01/03] Step [015/025]: cls_loss=0.6457
Epoch [01/03] Step [016/025]: cls_loss=0.6781
Epoch [01/03] Step [017/025]: cls_loss=0.5728
Epoch [01/03] Step [018/025]: cls_loss=0.7132
Epoch [01/03] Step [019/025]: cls_loss=0.6598
Epoch [01/03] Step [020/025]: cls_loss=0.6264
Epoch [01/03] Step [021/025]: cls_loss=0.6791
Epoch [01/03] Step [022/025]: cls_loss=0.6686
Epoch [01/03] Step [023/025]: cls_loss=0.6504
Epoch [01/03] Step [024/025]: cls_loss=0.6954
Epoch [01/03] Step [025/025]: cls_loss=0.7048
Epoch [02/03] Step [001/025]: cls_loss=0.6761
Epoch [02/03] Step [002/025]: cls_loss=0.6710
Epoch [02/03] Step [003/025]: cls_loss=0.6648
Epoch [02/03] Step [004/025]: cls_loss=0.6563
Epoch [02/03] Step [005/025]: cls_loss=0.6401
Epoch [02/03] Step [006/025]: cls_loss=0.6854
Epoch [02/03] Step [007/025]: cls_loss=0.7162
Epoch [02/03] Step [008/025]: cls_loss=0.6806
Epoch [02/03] Step [009/025]: cls_loss=0.6936
Epoch [02/03] Step [010/025]: cls_loss=0.6978
Epoch [02/03] Step [011/025]: cls_loss=0.6511
Epoch [02/03] Step [012/025]: cls_loss=0.6270
Epoch [02/03] Step [013/025]: cls_loss=0.6502
Epoch [02/03] Step [014/025]: cls_loss=0.6749
Epoch [02/03] Step [015/025]: cls_loss=0.6979
Epoch [02/03] Step [016/025]: cls_loss=0.5865
Epoch [02/03] Step [017/025]: cls_loss=0.6571
Epoch [02/03] Step [018/025]: cls_loss=0.7098
Epoch [02/03] Step [019/025]: cls_loss=0.6663
Epoch [02/03] Step [020/025]: cls_loss=0.6872
Epoch [02/03] Step [021/025]: cls_loss=0.7448
Epoch [02/03] Step [022/025]: cls_loss=0.6722
Epoch [02/03] Step [023/025]: cls_loss=0.7011
Epoch [02/03] Step [024/025]: cls_loss=0.6856
Epoch [02/03] Step [025/025]: cls_loss=0.6863
Epoch [03/03] Step [001/025]: cls_loss=0.6867
Epoch [03/03] Step [002/025]: cls_loss=0.6912
Epoch [03/03] Step [003/025]: cls_loss=0.6846
Epoch [03/03] Step [004/025]: cls_loss=0.6840
Epoch [03/03] Step [005/025]: cls_loss=0.6866
Epoch [03/03] Step [006/025]: cls_loss=0.6813
Epoch [03/03] Step [007/025]: cls_loss=0.6839
Epoch [03/03] Step [008/025]: cls_loss=0.6829
Epoch [03/03] Step [009/025]: cls_loss=0.6747
Epoch [03/03] Step [010/025]: cls_loss=0.6945
Epoch [03/03] Step [011/025]: cls_loss=0.6821
Epoch [03/03] Step [012/025]: cls_loss=0.6491
Epoch [03/03] Step [013/025]: cls_loss=0.6897
Epoch [03/03] Step [014/025]: cls_loss=0.6261
Epoch [03/03] Step [015/025]: cls_loss=0.7006
Epoch [03/03] Step [016/025]: cls_loss=0.7231
Epoch [03/03] Step [017/025]: cls_loss=0.6988
Epoch [03/03] Step [018/025]: cls_loss=0.6088
Epoch [03/03] Step [019/025]: cls_loss=0.7034
Epoch [03/03] Step [020/025]: cls_loss=0.6771
Epoch [03/03] Step [021/025]: cls_loss=0.6883
Epoch [03/03] Step [022/025]: cls_loss=0.6941
Epoch [03/03] Step [023/025]: cls_loss=0.6487
Epoch [03/03] Step [024/025]: cls_loss=0.6605
Epoch [03/03] Step [025/025]: cls_loss=0.6301
save pretrained model to: /content/snapshots/community/bert/42/source-encoder.pt
save pretrained model to: /content/snapshots/community/bert/42/source-classifier.pt
=== Evaluating classifier for source domain ===
Avg Loss = 0.6644, Avg Accuracy = 0.6088
Avg Loss = 0.6702, Avg Accuracy = 0.6025
Avg Loss = 0.6805, Avg Accuracy = 0.6050
=== Training encoder for target domain ===
^C

```
