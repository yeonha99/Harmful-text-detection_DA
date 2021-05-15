2021-05-15 08:29:28.905684: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
=== Argument Setting ===
src: community
tgt: news
seed: 42
train_seed: 42
model_type: kobert
max_seq_length: 128
batch_size: 32
pre_epochs: 3
num_epochs: 3
AD weight: 1.0
KD weight: 1.0
temperature: 20
=== Processing datasets ===
writing example 200 of 800
writing example 400 of 800
writing example 600 of 800
writing example 800 of 800
writing example 200 of 200
writing example 200 of 1000
writing example 400 of 1000
writing example 600 of 1000
writing example 800 of 1000
writing example 1000 of 1000
writing example 200 of 800
writing example 400 of 800
writing example 600 of 800
writing example 800 of 800
=== Training classifier for source domain ===
Epoch [01/03] Step [001/025]: cls_loss=0.6570
Epoch [01/03] Step [002/025]: cls_loss=0.6931
Epoch [01/03] Step [003/025]: cls_loss=0.6829
Epoch [01/03] Step [004/025]: cls_loss=0.7021
Epoch [01/03] Step [005/025]: cls_loss=0.6860
Epoch [01/03] Step [006/025]: cls_loss=0.7269
Epoch [01/03] Step [007/025]: cls_loss=0.6979
Epoch [01/03] Step [008/025]: cls_loss=0.7150
Epoch [01/03] Step [009/025]: cls_loss=0.6922
Epoch [01/03] Step [010/025]: cls_loss=0.7318
Epoch [01/03] Step [011/025]: cls_loss=0.7301
Epoch [01/03] Step [012/025]: cls_loss=0.6883
Epoch [01/03] Step [013/025]: cls_loss=0.6794
Epoch [01/03] Step [014/025]: cls_loss=0.7345
Epoch [01/03] Step [015/025]: cls_loss=0.7250
Epoch [01/03] Step [016/025]: cls_loss=0.7288
Epoch [01/03] Step [017/025]: cls_loss=0.7389
Epoch [01/03] Step [018/025]: cls_loss=0.6936
Epoch [01/03] Step [019/025]: cls_loss=0.6917
Epoch [01/03] Step [020/025]: cls_loss=0.6950
Epoch [01/03] Step [021/025]: cls_loss=0.7100
Epoch [01/03] Step [022/025]: cls_loss=0.7023
Epoch [01/03] Step [023/025]: cls_loss=0.7196
Epoch [01/03] Step [024/025]: cls_loss=0.7088
Epoch [01/03] Step [025/025]: cls_loss=0.6711
Epoch [02/03] Step [001/025]: cls_loss=0.6905
Epoch [02/03] Step [002/025]: cls_loss=0.6738
Epoch [02/03] Step [003/025]: cls_loss=0.6658
Epoch [02/03] Step [004/025]: cls_loss=0.6974
Epoch [02/03] Step [005/025]: cls_loss=0.7058
Epoch [02/03] Step [006/025]: cls_loss=0.6729
Epoch [02/03] Step [007/025]: cls_loss=0.7136
Epoch [02/03] Step [008/025]: cls_loss=0.6563
Epoch [02/03] Step [009/025]: cls_loss=0.6665
Epoch [02/03] Step [010/025]: cls_loss=0.6808
Epoch [02/03] Step [011/025]: cls_loss=0.6944
Epoch [02/03] Step [012/025]: cls_loss=0.6730
Epoch [02/03] Step [013/025]: cls_loss=0.6577
Epoch [02/03] Step [014/025]: cls_loss=0.7147
Epoch [02/03] Step [015/025]: cls_loss=0.6880
Epoch [02/03] Step [016/025]: cls_loss=0.6800
Epoch [02/03] Step [017/025]: cls_loss=0.7023
Epoch [02/03] Step [018/025]: cls_loss=0.6823
Epoch [02/03] Step [019/025]: cls_loss=0.6689
Epoch [02/03] Step [020/025]: cls_loss=0.6954
Epoch [02/03] Step [021/025]: cls_loss=0.7110
Epoch [02/03] Step [022/025]: cls_loss=0.7063
Epoch [02/03] Step [023/025]: cls_loss=0.6998
Epoch [02/03] Step [024/025]: cls_loss=0.6544
Epoch [02/03] Step [025/025]: cls_loss=0.6673
Epoch [03/03] Step [001/025]: cls_loss=0.6830
Epoch [03/03] Step [002/025]: cls_loss=0.6735
Epoch [03/03] Step [003/025]: cls_loss=0.7359
Epoch [03/03] Step [004/025]: cls_loss=0.7041
Epoch [03/03] Step [005/025]: cls_loss=0.6631
Epoch [03/03] Step [006/025]: cls_loss=0.6744
Epoch [03/03] Step [007/025]: cls_loss=0.6938
Epoch [03/03] Step [008/025]: cls_loss=0.6635
Epoch [03/03] Step [009/025]: cls_loss=0.7306
Epoch [03/03] Step [010/025]: cls_loss=0.7670
Epoch [03/03] Step [011/025]: cls_loss=0.7221
Epoch [03/03] Step [012/025]: cls_loss=0.6668
Epoch [03/03] Step [013/025]: cls_loss=0.7079
Epoch [03/03] Step [014/025]: cls_loss=0.6881
Epoch [03/03] Step [015/025]: cls_loss=0.7022
Epoch [03/03] Step [016/025]: cls_loss=0.6701
Epoch [03/03] Step [017/025]: cls_loss=0.6516
Epoch [03/03] Step [018/025]: cls_loss=0.6657
Epoch [03/03] Step [019/025]: cls_loss=0.6611
Epoch [03/03] Step [020/025]: cls_loss=0.6512
Epoch [03/03] Step [021/025]: cls_loss=0.7083
Epoch [03/03] Step [022/025]: cls_loss=0.6260
Epoch [03/03] Step [023/025]: cls_loss=0.6621
Epoch [03/03] Step [024/025]: cls_loss=0.6739
Epoch [03/03] Step [025/025]: cls_loss=0.6469
save pretrained model to: /content/snapshots/community/kobert/42/source-encoder.pt
save pretrained model to: /content/snapshots/community/kobert/42/source-classifier.pt
=== Evaluating classifier for source domain ===
Avg Loss = 0.7042, Avg Accuracy = 0.5575
Avg Loss = 0.7217, Avg Accuracy = 0.5350
Avg Loss = 0.7212, Avg Accuracy = 0.5290
=== Training encoder for target domain ===
Epoch [01/03] Step [001/025]: acc=0.5000 g_loss=0.6909 d_loss=0.6927 kd_loss=0.0140
Epoch [01/03] Step [002/025]: acc=0.5000 g_loss=0.6853 d_loss=0.6931 kd_loss=0.0052
Epoch [01/03] Step [003/025]: acc=0.5000 g_loss=0.6851 d_loss=0.6932 kd_loss=0.0132
Epoch [01/03] Step [004/025]: acc=0.5000 g_loss=0.6891 d_loss=0.6937 kd_loss=0.0057
Epoch [01/03] Step [005/025]: acc=0.5000 g_loss=0.6928 d_loss=0.6917 kd_loss=0.0081
Epoch [01/03] Step [006/025]: acc=0.5000 g_loss=0.6947 d_loss=0.6921 kd_loss=0.0063
Epoch [01/03] Step [007/025]: acc=0.5000 g_loss=0.6927 d_loss=0.6925 kd_loss=0.0100
Epoch [01/03] Step [008/025]: acc=0.5000 g_loss=0.6904 d_loss=0.6953 kd_loss=0.0156
Epoch [01/03] Step [009/025]: acc=0.5000 g_loss=0.6965 d_loss=0.6916 kd_loss=0.0158
Epoch [01/03] Step [010/025]: acc=0.5000 g_loss=0.6962 d_loss=0.6918 kd_loss=0.0060
Epoch [01/03] Step [011/025]: acc=0.5000 g_loss=0.6928 d_loss=0.6931 kd_loss=0.0042
Epoch [01/03] Step [012/025]: acc=0.5000 g_loss=0.6832 d_loss=0.6962 kd_loss=0.0041
Epoch [01/03] Step [013/025]: acc=0.5000 g_loss=0.6778 d_loss=0.6897 kd_loss=0.0087
Epoch [01/03] Step [014/025]: acc=0.5000 g_loss=0.6699 d_loss=0.6972 kd_loss=0.0096
Epoch [01/03] Step [015/025]: acc=0.5000 g_loss=0.6697 d_loss=0.6940 kd_loss=0.0146
Epoch [01/03] Step [016/025]: acc=0.5000 g_loss=0.6737 d_loss=0.6930 kd_loss=0.0068
Epoch [01/03] Step [017/025]: acc=0.5000 g_loss=0.6748 d_loss=0.6929 kd_loss=0.0099
Epoch [01/03] Step [018/025]: acc=0.5000 g_loss=0.6753 d_loss=0.6935 kd_loss=0.0155
Epoch [01/03] Step [019/025]: acc=0.5000 g_loss=0.6781 d_loss=0.6935 kd_loss=0.0049
Epoch [01/03] Step [020/025]: acc=0.5000 g_loss=0.6829 d_loss=0.6926 kd_loss=0.0068
Epoch [01/03] Step [021/025]: acc=0.5000 g_loss=0.6843 d_loss=0.6924 kd_loss=0.0066
Epoch [01/03] Step [022/025]: acc=0.5000 g_loss=0.6835 d_loss=0.6927 kd_loss=0.0062
Epoch [01/03] Step [023/025]: acc=0.5000 g_loss=0.6829 d_loss=0.6945 kd_loss=0.0098
Epoch [01/03] Step [024/025]: acc=0.5000 g_loss=0.6863 d_loss=0.6944 kd_loss=0.0129
Epoch [01/03] Step [025/025]: acc=0.5000 g_loss=0.6874 d_loss=0.6933 kd_loss=0.0100
Avg Loss = 0.7306, Avg Accuracy = 0.5300
Epoch [02/03] Step [001/025]: acc=0.5000 g_loss=0.6853 d_loss=0.6932 kd_loss=0.0052
Epoch [02/03] Step [002/025]: acc=0.5000 g_loss=0.6842 d_loss=0.6944 kd_loss=0.0037
Epoch [02/03] Step [003/025]: acc=0.5000 g_loss=0.6861 d_loss=0.6932 kd_loss=0.0098
Epoch [02/03] Step [004/025]: acc=0.5000 g_loss=0.6876 d_loss=0.6934 kd_loss=0.0122
Epoch [02/03] Step [005/025]: acc=0.5000 g_loss=0.6887 d_loss=0.6932 kd_loss=0.0054
Epoch [02/03] Step [006/025]: acc=0.5000 g_loss=0.6889 d_loss=0.6932 kd_loss=0.0081
Epoch [02/03] Step [007/025]: acc=0.5000 g_loss=0.6886 d_loss=0.6936 kd_loss=0.0138
Epoch [02/03] Step [008/025]: acc=0.5000 g_loss=0.6900 d_loss=0.6930 kd_loss=0.0056
Epoch [02/03] Step [009/025]: acc=0.5000 g_loss=0.6911 d_loss=0.6929 kd_loss=0.0098
Epoch [02/03] Step [010/025]: acc=0.5000 g_loss=0.6914 d_loss=0.6947 kd_loss=0.0072
Epoch [02/03] Step [011/025]: acc=0.5000 g_loss=0.6921 d_loss=0.6933 kd_loss=0.0117
Epoch [02/03] Step [012/025]: acc=0.5000 g_loss=0.6933 d_loss=0.6935 kd_loss=0.0048
Epoch [02/03] Step [013/025]: acc=0.5000 g_loss=0.6902 d_loss=0.6931 kd_loss=0.0047
Epoch [02/03] Step [014/025]: acc=0.5000 g_loss=0.6887 d_loss=0.6935 kd_loss=0.0091
Epoch [02/03] Step [015/025]: acc=0.5000 g_loss=0.6898 d_loss=0.6933 kd_loss=0.0043
Epoch [02/03] Step [016/025]: acc=0.5000 g_loss=0.6904 d_loss=0.6941 kd_loss=0.0044
Epoch [02/03] Step [017/025]: acc=0.5000 g_loss=0.6897 d_loss=0.6932 kd_loss=0.0060
Epoch [02/03] Step [018/025]: acc=0.5000 g_loss=0.6882 d_loss=0.6935 kd_loss=0.0045
Epoch [02/03] Step [019/025]: acc=0.5000 g_loss=0.6877 d_loss=0.6927 kd_loss=0.0049
Epoch [02/03] Step [020/025]: acc=0.5000 g_loss=0.6891 d_loss=0.6932 kd_loss=0.0073
Epoch [02/03] Step [021/025]: acc=0.5000 g_loss=0.6897 d_loss=0.6925 kd_loss=0.0021
Epoch [02/03] Step [022/025]: acc=0.5000 g_loss=0.6875 d_loss=0.6923 kd_loss=0.0009
Epoch [02/03] Step [023/025]: acc=0.5000 g_loss=0.6852 d_loss=0.6946 kd_loss=0.0084
Epoch [02/03] Step [024/025]: acc=0.5000 g_loss=0.6848 d_loss=0.6927 kd_loss=0.0087
Epoch [02/03] Step [025/025]: acc=0.5000 g_loss=0.6841 d_loss=0.6952 kd_loss=0.0024
Avg Loss = 0.7186, Avg Accuracy = 0.5300
Epoch [03/03] Step [001/025]: acc=0.5000 g_loss=0.6862 d_loss=0.6937 kd_loss=0.0011
Epoch [03/03] Step [002/025]: acc=0.5000 g_loss=0.6862 d_loss=0.6946 kd_loss=0.0008
Epoch [03/03] Step [003/025]: acc=0.5000 g_loss=0.6886 d_loss=0.6937 kd_loss=0.0044
Epoch [03/03] Step [004/025]: acc=0.5000 g_loss=0.6886 d_loss=0.6937 kd_loss=0.0044
Epoch [03/03] Step [005/025]: acc=0.5000 g_loss=0.6898 d_loss=0.6932 kd_loss=0.0046
Epoch [03/03] Step [006/025]: acc=0.5000 g_loss=0.6920 d_loss=0.6933 kd_loss=0.0086
Epoch [03/03] Step [007/025]: acc=0.5000 g_loss=0.6928 d_loss=0.6922 kd_loss=0.0076
Epoch [03/03] Step [008/025]: acc=0.5000 g_loss=0.6925 d_loss=0.6926 kd_loss=0.0011
Epoch [03/03] Step [009/025]: acc=0.5000 g_loss=0.6919 d_loss=0.6929 kd_loss=0.0005
Epoch [03/03] Step [010/025]: acc=0.5000 g_loss=0.6886 d_loss=0.6930 kd_loss=0.0005
Epoch [03/03] Step [011/025]: acc=0.5000 g_loss=0.6873 d_loss=0.6924 kd_loss=0.0005
Epoch [03/03] Step [012/025]: acc=0.5000 g_loss=0.6861 d_loss=0.6918 kd_loss=0.0025
Epoch [03/03] Step [013/025]: acc=0.5000 g_loss=0.6787 d_loss=0.6933 kd_loss=0.0008
Epoch [03/03] Step [014/025]: acc=0.5000 g_loss=0.6745 d_loss=0.6927 kd_loss=0.0088
Epoch [03/03] Step [015/025]: acc=0.5000 g_loss=0.6646 d_loss=0.6940 kd_loss=0.0035
Epoch [03/03] Step [016/025]: acc=0.5000 g_loss=0.6573 d_loss=0.6944 kd_loss=0.0034
Epoch [03/03] Step [017/025]: acc=0.5000 g_loss=0.6566 d_loss=0.6940 kd_loss=0.0046
Epoch [03/03] Step [018/025]: acc=0.5000 g_loss=0.6620 d_loss=0.6938 kd_loss=0.0067
Epoch [03/03] Step [019/025]: acc=0.5000 g_loss=0.6704 d_loss=0.6939 kd_loss=0.0057
Epoch [03/03] Step [020/025]: acc=0.5000 g_loss=0.6794 d_loss=0.6939 kd_loss=0.0075
Epoch [03/03] Step [021/025]: acc=0.5000 g_loss=0.6912 d_loss=0.6928 kd_loss=0.0047
Epoch [03/03] Step [022/025]: acc=0.5000 g_loss=0.6998 d_loss=0.6931 kd_loss=0.0022
Epoch [03/03] Step [023/025]: acc=0.5000 g_loss=0.7059 d_loss=0.6940 kd_loss=0.0060
Epoch [03/03] Step [024/025]: acc=0.5000 g_loss=0.7116 d_loss=0.6930 kd_loss=0.0049
Epoch [03/03] Step [025/025]: acc=0.5000 g_loss=0.7121 d_loss=0.6937 kd_loss=0.0038
Avg Loss = 0.7374, Avg Accuracy = 0.5310
=== Evaluating classifier for encoded target domain ===
>>> source only <<<
Avg Loss = 0.7207, Avg Accuracy = 0.5290
>>> domain adaption <<<
Avg Loss = 0.7357, Avg Accuracy = 0.5310
