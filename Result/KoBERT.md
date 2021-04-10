```

(torch) P1ZZ4:bert-AAD_kobert p1zz4$ python main.py --pretrain --adapt --src community --tgt news
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
=== Training classifier for source domain ===
Epoch [01/03] Step [001/025]: cls_loss=0.6931
Epoch [01/03] Step [002/025]: cls_loss=0.7009
Epoch [01/03] Step [003/025]: cls_loss=0.6581
Epoch [01/03] Step [004/025]: cls_loss=0.6703
Epoch [01/03] Step [005/025]: cls_loss=0.6447
Epoch [01/03] Step [006/025]: cls_loss=0.7170
Epoch [01/03] Step [007/025]: cls_loss=0.6980
Epoch [01/03] Step [008/025]: cls_loss=0.6832
Epoch [01/03] Step [009/025]: cls_loss=0.7054
Epoch [01/03] Step [010/025]: cls_loss=0.7063
Epoch [01/03] Step [011/025]: cls_loss=0.6930
Epoch [01/03] Step [012/025]: cls_loss=0.6813
Epoch [01/03] Step [013/025]: cls_loss=0.6753
Epoch [01/03] Step [014/025]: cls_loss=0.6761
Epoch [01/03] Step [015/025]: cls_loss=0.6539
Epoch [01/03] Step [016/025]: cls_loss=0.6754
Epoch [01/03] Step [017/025]: cls_loss=0.6103
Epoch [01/03] Step [018/025]: cls_loss=0.6736
Epoch [01/03] Step [019/025]: cls_loss=0.6444
Epoch [01/03] Step [020/025]: cls_loss=0.6247
Epoch [01/03] Step [021/025]: cls_loss=0.6846
Epoch [01/03] Step [022/025]: cls_loss=0.6748
Epoch [01/03] Step [023/025]: cls_loss=0.6708
Epoch [01/03] Step [024/025]: cls_loss=0.7572
Epoch [01/03] Step [025/025]: cls_loss=0.7557
Epoch [02/03] Step [001/025]: cls_loss=0.6548
Epoch [02/03] Step [002/025]: cls_loss=0.6523
Epoch [02/03] Step [003/025]: cls_loss=0.6783
Epoch [02/03] Step [004/025]: cls_loss=0.6545
Epoch [02/03] Step [005/025]: cls_loss=0.6582
Epoch [02/03] Step [006/025]: cls_loss=0.6823
Epoch [02/03] Step [007/025]: cls_loss=0.6835
Epoch [02/03] Step [008/025]: cls_loss=0.6818
Epoch [02/03] Step [009/025]: cls_loss=0.6792
Epoch [02/03] Step [010/025]: cls_loss=0.6917
Epoch [02/03] Step [011/025]: cls_loss=0.6653
Epoch [02/03] Step [012/025]: cls_loss=0.6514
Epoch [02/03] Step [013/025]: cls_loss=0.6534
Epoch [02/03] Step [014/025]: cls_loss=0.6759
Epoch [02/03] Step [015/025]: cls_loss=0.6879
Epoch [02/03] Step [016/025]: cls_loss=0.6140
Epoch [02/03] Step [017/025]: cls_loss=0.6647
Epoch [02/03] Step [018/025]: cls_loss=0.7062
Epoch [02/03] Step [019/025]: cls_loss=0.6760
Epoch [02/03] Step [020/025]: cls_loss=0.6873
Epoch [02/03] Step [021/025]: cls_loss=0.7698
Epoch [02/03] Step [022/025]: cls_loss=0.6849
Epoch [02/03] Step [023/025]: cls_loss=0.7042
Epoch [02/03] Step [024/025]: cls_loss=0.7022
Epoch [02/03] Step [025/025]: cls_loss=0.6794
Epoch [03/03] Step [001/025]: cls_loss=0.6780
Epoch [03/03] Step [002/025]: cls_loss=0.6926
Epoch [03/03] Step [003/025]: cls_loss=0.6776
Epoch [03/03] Step [004/025]: cls_loss=0.6895
Epoch [03/03] Step [005/025]: cls_loss=0.6831
Epoch [03/03] Step [006/025]: cls_loss=0.6830
Epoch [03/03] Step [007/025]: cls_loss=0.6803
Epoch [03/03] Step [008/025]: cls_loss=0.6838
Epoch [03/03] Step [009/025]: cls_loss=0.6840
Epoch [03/03] Step [010/025]: cls_loss=0.6948
Epoch [03/03] Step [011/025]: cls_loss=0.6772
Epoch [03/03] Step [012/025]: cls_loss=0.6623
Epoch [03/03] Step [013/025]: cls_loss=0.6892
Epoch [03/03] Step [014/025]: cls_loss=0.6423
Epoch [03/03] Step [015/025]: cls_loss=0.6991
Epoch [03/03] Step [016/025]: cls_loss=0.7138
Epoch [03/03] Step [017/025]: cls_loss=0.7128
Epoch [03/03] Step [018/025]: cls_loss=0.6063
Epoch [03/03] Step [019/025]: cls_loss=0.7233
Epoch [03/03] Step [020/025]: cls_loss=0.6855
Epoch [03/03] Step [021/025]: cls_loss=0.6800
Epoch [03/03] Step [022/025]: cls_loss=0.6923
Epoch [03/03] Step [023/025]: cls_loss=0.6352
Epoch [03/03] Step [024/025]: cls_loss=0.6659
Epoch [03/03] Step [025/025]: cls_loss=0.6265
save pretrained model to: snapshots/community/bert/42/source-encoder.pt
save pretrained model to: snapshots/community/bert/42/source-classifier.pt
=== Evaluating classifier for source domain ===
Avg Loss = 0.6719, Avg Accuracy = 0.6038
Avg Loss = 0.6735, Avg Accuracy = 0.6050
Avg Loss = 0.6709, Avg Accuracy = 0.6040
=== Training encoder for target domain ===
Epoch [01/03] Step [001/025]: acc=0.5000 g_loss=0.6894 d_loss=0.6933 kd_loss=0.0005
Epoch [01/03] Step [002/025]: acc=0.5000 g_loss=0.6908 d_loss=0.6931 kd_loss=0.0002
Epoch [01/03] Step [003/025]: acc=0.5000 g_loss=0.6905 d_loss=0.6930 kd_loss=0.0004
Epoch [01/03] Step [004/025]: acc=0.5000 g_loss=0.6897 d_loss=0.6932 kd_loss=0.0001
Epoch [01/03] Step [005/025]: acc=0.5000 g_loss=0.6912 d_loss=0.6930 kd_loss=0.0001
Epoch [01/03] Step [006/025]: acc=0.5000 g_loss=0.6905 d_loss=0.6933 kd_loss=0.0002
Epoch [01/03] Step [007/025]: acc=0.5000 g_loss=0.6895 d_loss=0.6934 kd_loss=0.0002
Epoch [01/03] Step [008/025]: acc=0.5000 g_loss=0.6863 d_loss=0.6936 kd_loss=0.0001
Epoch [01/03] Step [009/025]: acc=0.5000 g_loss=0.6858 d_loss=0.6930 kd_loss=0.0001
Epoch [01/03] Step [010/025]: acc=0.5000 g_loss=0.6852 d_loss=0.6932 kd_loss=0.0001
Epoch [01/03] Step [011/025]: acc=0.5000 g_loss=0.6849 d_loss=0.6932 kd_loss=0.0002
Epoch [01/03] Step [012/025]: acc=0.5000 g_loss=0.6854 d_loss=0.6932 kd_loss=0.0001
Epoch [01/03] Step [013/025]: acc=0.5000 g_loss=0.6864 d_loss=0.6931 kd_loss=0.0002
Epoch [01/03] Step [014/025]: acc=0.5000 g_loss=0.6874 d_loss=0.6933 kd_loss=0.0001
Epoch [01/03] Step [015/025]: acc=0.5000 g_loss=0.6878 d_loss=0.6934 kd_loss=0.0001
Epoch [01/03] Step [016/025]: acc=0.5000 g_loss=0.6892 d_loss=0.6930 kd_loss=0.0002
Epoch [01/03] Step [017/025]: acc=0.5000 g_loss=0.6911 d_loss=0.6928 kd_loss=0.0004
Epoch [01/03] Step [018/025]: acc=0.5000 g_loss=0.6937 d_loss=0.6921 kd_loss=0.0002
Epoch [01/03] Step [019/025]: acc=0.5000 g_loss=0.6954 d_loss=0.6922 kd_loss=0.0001
Epoch [01/03] Step [020/025]: acc=0.5000 g_loss=0.6955 d_loss=0.6926 kd_loss=0.0001
Epoch [01/03] Step [021/025]: acc=0.5000 g_loss=0.6959 d_loss=0.6925 kd_loss=0.0001
Epoch [01/03] Step [022/025]: acc=0.5000 g_loss=0.6961 d_loss=0.6922 kd_loss=0.0002
Epoch [01/03] Step [023/025]: acc=0.5000 g_loss=0.6970 d_loss=0.6937 kd_loss=0.0002
Epoch [01/03] Step [024/025]: acc=0.5000 g_loss=0.6933 d_loss=0.6939 kd_loss=0.0002
Epoch [01/03] Step [025/025]: acc=0.5000 g_loss=0.6921 d_loss=0.6944 kd_loss=0.0004
Avg Loss = 0.6719, Avg Accuracy = 0.6040
Epoch [02/03] Step [001/025]: acc=0.5000 g_loss=0.6976 d_loss=0.6932 kd_loss=0.0001
Epoch [02/03] Step [002/025]: acc=0.5000 g_loss=0.6931 d_loss=0.6932 kd_loss=0.0002
Epoch [02/03] Step [003/025]: acc=0.5000 g_loss=0.6872 d_loss=0.6932 kd_loss=0.0003
Epoch [02/03] Step [004/025]: acc=0.5000 g_loss=0.6789 d_loss=0.6933 kd_loss=0.0002
Epoch [02/03] Step [005/025]: acc=0.5000 g_loss=0.6711 d_loss=0.6935 kd_loss=0.0001
Epoch [02/03] Step [006/025]: acc=0.5000 g_loss=0.6661 d_loss=0.6936 kd_loss=0.0000
Epoch [02/03] Step [007/025]: acc=0.5000 g_loss=0.6639 d_loss=0.6937 kd_loss=0.0000
Epoch [02/03] Step [008/025]: acc=0.5000 g_loss=0.6634 d_loss=0.6938 kd_loss=-0.0000
Epoch [02/03] Step [009/025]: acc=0.5000 g_loss=0.6641 d_loss=0.6937 kd_loss=-0.0000
Epoch [02/03] Step [010/025]: acc=0.5000 g_loss=0.6662 d_loss=0.6938 kd_loss=0.0000
Epoch [02/03] Step [011/025]: acc=0.5000 g_loss=0.6695 d_loss=0.6936 kd_loss=0.0001
Epoch [02/03] Step [012/025]: acc=0.5000 g_loss=0.6738 d_loss=0.6936 kd_loss=0.0003
Epoch [02/03] Step [013/025]: acc=0.5000 g_loss=0.6790 d_loss=0.6934 kd_loss=0.0005
Epoch [02/03] Step [014/025]: acc=0.5000 g_loss=0.6847 d_loss=0.6933 kd_loss=0.0006
Epoch [02/03] Step [015/025]: acc=0.5000 g_loss=0.6903 d_loss=0.6933 kd_loss=0.0007
Epoch [02/03] Step [016/025]: acc=0.5000 g_loss=0.6957 d_loss=0.6932 kd_loss=0.0006
Epoch [02/03] Step [017/025]: acc=0.5000 g_loss=0.7003 d_loss=0.6932 kd_loss=0.0005
Epoch [02/03] Step [018/025]: acc=0.5000 g_loss=0.7032 d_loss=0.6932 kd_loss=0.0003
Epoch [02/03] Step [019/025]: acc=0.5000 g_loss=0.7020 d_loss=0.6938 kd_loss=0.0001
Epoch [02/03] Step [020/025]: acc=0.5000 g_loss=0.6853 d_loss=0.6942 kd_loss=0.0195
Epoch [02/03] Step [021/025]: acc=0.5000 g_loss=0.6852 d_loss=0.6959 kd_loss=0.0069
Epoch [02/03] Step [022/025]: acc=0.5000 g_loss=0.6905 d_loss=0.6947 kd_loss=0.0008
Epoch [02/03] Step [023/025]: acc=0.5000 g_loss=0.6916 d_loss=0.6941 kd_loss=0.0003
Epoch [02/03] Step [024/025]: acc=0.5000 g_loss=0.6909 d_loss=0.6938 kd_loss=0.0002
Epoch [02/03] Step [025/025]: acc=0.5000 g_loss=0.6896 d_loss=0.6940 kd_loss=0.0004
Avg Loss = 0.6744, Avg Accuracy = 0.6040
Epoch [03/03] Step [001/025]: acc=0.5000 g_loss=0.6902 d_loss=0.6936 kd_loss=0.0005
Epoch [03/03] Step [002/025]: acc=0.5000 g_loss=0.6914 d_loss=0.6934 kd_loss=0.0005
Epoch [03/03] Step [003/025]: acc=0.5000 g_loss=0.6923 d_loss=0.6931 kd_loss=0.0005
Epoch [03/03] Step [004/025]: acc=0.5000 g_loss=0.6926 d_loss=0.6929 kd_loss=0.0002
Epoch [03/03] Step [005/025]: acc=0.5000 g_loss=0.6921 d_loss=0.6930 kd_loss=0.0001
Epoch [03/03] Step [006/025]: acc=0.5000 g_loss=0.6920 d_loss=0.6930 kd_loss=0.0000
Epoch [03/03] Step [007/025]: acc=0.5000 g_loss=0.6920 d_loss=0.6931 kd_loss=-0.0000
Epoch [03/03] Step [008/025]: acc=0.5000 g_loss=0.6922 d_loss=0.6931 kd_loss=-0.0000
Epoch [03/03] Step [009/025]: acc=0.5000 g_loss=0.6921 d_loss=0.6931 kd_loss=0.0000
Epoch [03/03] Step [010/025]: acc=0.5000 g_loss=0.6919 d_loss=0.6931 kd_loss=0.0001
Epoch [03/03] Step [011/025]: acc=0.5000 g_loss=0.6917 d_loss=0.6932 kd_loss=0.0001
Epoch [03/03] Step [012/025]: acc=0.5000 g_loss=0.6914 d_loss=0.6932 kd_loss=0.0002
Epoch [03/03] Step [013/025]: acc=0.5000 g_loss=0.6912 d_loss=0.6931 kd_loss=0.0002
Epoch [03/03] Step [014/025]: acc=0.5000 g_loss=0.6910 d_loss=0.6932 kd_loss=0.0003
Epoch [03/03] Step [015/025]: acc=0.5000 g_loss=0.6910 d_loss=0.6932 kd_loss=0.0003
Epoch [03/03] Step [016/025]: acc=0.5000 g_loss=0.6910 d_loss=0.6932 kd_loss=0.0002
Epoch [03/03] Step [017/025]: acc=0.5000 g_loss=0.6911 d_loss=0.6932 kd_loss=0.0002
Epoch [03/03] Step [018/025]: acc=0.5000 g_loss=0.6913 d_loss=0.6932 kd_loss=0.0001
Epoch [03/03] Step [019/025]: acc=0.5000 g_loss=0.6915 d_loss=0.6932 kd_loss=0.0001
Epoch [03/03] Step [020/025]: acc=0.5000 g_loss=0.6918 d_loss=0.6931 kd_loss=0.0000
Epoch [03/03] Step [021/025]: acc=0.5000 g_loss=0.6921 d_loss=0.6931 kd_loss=0.0000
Epoch [03/03] Step [022/025]: acc=0.5000 g_loss=0.6925 d_loss=0.6931 kd_loss=-0.0000
Epoch [03/03] Step [023/025]: acc=0.5000 g_loss=0.6929 d_loss=0.6931 kd_loss=-0.0000
Epoch [03/03] Step [024/025]: acc=0.5000 g_loss=0.6933 d_loss=0.6931 kd_loss=0.0000
Epoch [03/03] Step [025/025]: acc=0.5000 g_loss=0.6936 d_loss=0.6931 kd_loss=0.0000
Avg Loss = 0.6733, Avg Accuracy = 0.6040
=== Evaluating classifier for encoded target domain ===
>>> source only <<<
Avg Loss = 0.6723, Avg Accuracy = 0.6040
>>> domain adaption <<<
Avg Loss = 0.6720, Avg Accuracy = 0.6040

```
