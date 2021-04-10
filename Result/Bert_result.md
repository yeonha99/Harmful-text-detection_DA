Last login: Thu Apr  8 21:51:14 on ttys000

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) P1ZZ4:~ p1zz4$ conda activate torch
(torch) P1ZZ4:~ p1zz4$ cd _________jongsul/
(torch) P1ZZ4:_________jongsul p1zz4$ ls
bert-AAD-master		news1.csv		train.tsv
community.csv		pretraing.txt		train_2.csv
community1.csv		pretraining_tsv.ipynb	train_3.csv
final.csv		splitpoint.ipynb	train_4.csv
news.csv		train.csv		train_label.csv
(torch) P1ZZ4:_________jongsul p1zz4$ cd bert-AAD-master/
(torch) P1ZZ4:bert-AAD-master p1zz4$ 
(torch) P1ZZ4:bert-AAD-master p1zz4$ ls
README.md	data		model.py	train.py
__pycache__	main.py		param.py	utils.py
(torch) P1ZZ4:bert-AAD-master p1zz4$ python main.py --pretrain --adapt
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
Epoch [01/03] Step [001/025]: cls_loss=0.8162
Epoch [01/03] Step [002/025]: cls_loss=0.7579
Epoch [01/03] Step [003/025]: cls_loss=0.6863
Epoch [01/03] Step [004/025]: cls_loss=0.6681
Epoch [01/03] Step [005/025]: cls_loss=0.6833
Epoch [01/03] Step [006/025]: cls_loss=0.6867
Epoch [01/03] Step [007/025]: cls_loss=0.7337
Epoch [01/03] Step [008/025]: cls_loss=0.6673
Epoch [01/03] Step [009/025]: cls_loss=0.7158
Epoch [01/03] Step [010/025]: cls_loss=0.6649
Epoch [01/03] Step [011/025]: cls_loss=0.7071
Epoch [01/03] Step [012/025]: cls_loss=0.6665
Epoch [01/03] Step [013/025]: cls_loss=0.6618
Epoch [01/03] Step [014/025]: cls_loss=0.7099
Epoch [01/03] Step [015/025]: cls_loss=0.6628
Epoch [01/03] Step [016/025]: cls_loss=0.6707
Epoch [01/03] Step [017/025]: cls_loss=0.6894
Epoch [01/03] Step [018/025]: cls_loss=0.6974
Epoch [01/03] Step [019/025]: cls_loss=0.6787
Epoch [01/03] Step [020/025]: cls_loss=0.6692
Epoch [01/03] Step [021/025]: cls_loss=0.6993
Epoch [01/03] Step [022/025]: cls_loss=0.6910
Epoch [01/03] Step [023/025]: cls_loss=0.6654
Epoch [01/03] Step [024/025]: cls_loss=0.6915
Epoch [01/03] Step [025/025]: cls_loss=0.7053
Epoch [02/03] Step [001/025]: cls_loss=0.6748
Epoch [02/03] Step [002/025]: cls_loss=0.6506
Epoch [02/03] Step [003/025]: cls_loss=0.6914
Epoch [02/03] Step [004/025]: cls_loss=0.6953
Epoch [02/03] Step [005/025]: cls_loss=0.6180
Epoch [02/03] Step [006/025]: cls_loss=0.7016
Epoch [02/03] Step [007/025]: cls_loss=0.7072
Epoch [02/03] Step [008/025]: cls_loss=0.7078
Epoch [02/03] Step [009/025]: cls_loss=0.6580
Epoch [02/03] Step [010/025]: cls_loss=0.6911
Epoch [02/03] Step [011/025]: cls_loss=0.6842
Epoch [02/03] Step [012/025]: cls_loss=0.6730
Epoch [02/03] Step [013/025]: cls_loss=0.6844
Epoch [02/03] Step [014/025]: cls_loss=0.7338
Epoch [02/03] Step [015/025]: cls_loss=0.7172
Epoch [02/03] Step [016/025]: cls_loss=0.6879
Epoch [02/03] Step [017/025]: cls_loss=0.6979
Epoch [02/03] Step [018/025]: cls_loss=0.6963
Epoch [02/03] Step [019/025]: cls_loss=0.6702
Epoch [02/03] Step [020/025]: cls_loss=0.6952
Epoch [02/03] Step [021/025]: cls_loss=0.6842
Epoch [02/03] Step [022/025]: cls_loss=0.6694
Epoch [02/03] Step [023/025]: cls_loss=0.6554
Epoch [02/03] Step [024/025]: cls_loss=0.6991
Epoch [02/03] Step [025/025]: cls_loss=0.6490
Epoch [03/03] Step [001/025]: cls_loss=0.6338
Epoch [03/03] Step [002/025]: cls_loss=0.6621
Epoch [03/03] Step [003/025]: cls_loss=0.6657
Epoch [03/03] Step [004/025]: cls_loss=0.6583
Epoch [03/03] Step [005/025]: cls_loss=0.6928
Epoch [03/03] Step [006/025]: cls_loss=0.7000
Epoch [03/03] Step [007/025]: cls_loss=0.7341
Epoch [03/03] Step [008/025]: cls_loss=0.7271
Epoch [03/03] Step [009/025]: cls_loss=0.7010
Epoch [03/03] Step [010/025]: cls_loss=0.6520
Epoch [03/03] Step [011/025]: cls_loss=0.6727
Epoch [03/03] Step [012/025]: cls_loss=0.6731
Epoch [03/03] Step [013/025]: cls_loss=0.6815
Epoch [03/03] Step [014/025]: cls_loss=0.6976
Epoch [03/03] Step [015/025]: cls_loss=0.6617
Epoch [03/03] Step [016/025]: cls_loss=0.6764
Epoch [03/03] Step [017/025]: cls_loss=0.6801
Epoch [03/03] Step [018/025]: cls_loss=0.6864
Epoch [03/03] Step [019/025]: cls_loss=0.6923
Epoch [03/03] Step [020/025]: cls_loss=0.6408
Epoch [03/03] Step [021/025]: cls_loss=0.6938
Epoch [03/03] Step [022/025]: cls_loss=0.6937
Epoch [03/03] Step [023/025]: cls_loss=0.6374
Epoch [03/03] Step [024/025]: cls_loss=0.7317
Epoch [03/03] Step [025/025]: cls_loss=0.6619
save pretrained model to: snapshots/community/bert/42/source-encoder.pt
save pretrained model to: snapshots/community/bert/42/source-classifier.pt
=== Evaluating classifier for source domain ===
Avg Loss = 0.6740, Avg Accuracy = 0.5988
Avg Loss = 0.6694, Avg Accuracy = 0.6250
Avg Loss = 0.6691, Avg Accuracy = 0.6040
=== Training encoder for target domain ===
Epoch [01/03] Step [001/025]: acc=0.5000 g_loss=0.7003 d_loss=0.6927 kd_loss=0.0008
Epoch [01/03] Step [002/025]: acc=0.5000 g_loss=0.6979 d_loss=0.6931 kd_loss=0.0003
Epoch [01/03] Step [003/025]: acc=0.5000 g_loss=0.6968 d_loss=0.6933 kd_loss=0.0002
Epoch [01/03] Step [004/025]: acc=0.5000 g_loss=0.6950 d_loss=0.6930 kd_loss=0.0003
Epoch [01/03] Step [005/025]: acc=0.5000 g_loss=0.6932 d_loss=0.6931 kd_loss=0.0002
Epoch [01/03] Step [006/025]: acc=0.5000 g_loss=0.6929 d_loss=0.6931 kd_loss=0.0002
Epoch [01/03] Step [007/025]: acc=0.5000 g_loss=0.6937 d_loss=0.6931 kd_loss=0.0002
Epoch [01/03] Step [008/025]: acc=0.5000 g_loss=0.6951 d_loss=0.6930 kd_loss=0.0002
Epoch [01/03] Step [009/025]: acc=0.5000 g_loss=0.6972 d_loss=0.6927 kd_loss=0.0002
Epoch [01/03] Step [010/025]: acc=0.5000 g_loss=0.6986 d_loss=0.6924 kd_loss=0.0002
Epoch [01/03] Step [011/025]: acc=0.5000 g_loss=0.6970 d_loss=0.6928 kd_loss=0.0003
Epoch [01/03] Step [012/025]: acc=0.5000 g_loss=0.6944 d_loss=0.6927 kd_loss=0.0003
Epoch [01/03] Step [013/025]: acc=0.5000 g_loss=0.6930 d_loss=0.6919 kd_loss=0.0005
Epoch [01/03] Step [014/025]: acc=0.5000 g_loss=0.6898 d_loss=0.6925 kd_loss=0.0006
Epoch [01/03] Step [015/025]: acc=0.5000 g_loss=0.6859 d_loss=0.6919 kd_loss=0.0008
Epoch [01/03] Step [016/025]: acc=0.5000 g_loss=0.6790 d_loss=0.6930 kd_loss=0.0013
Epoch [01/03] Step [017/025]: acc=0.5000 g_loss=0.6743 d_loss=0.6923 kd_loss=0.0015
Epoch [01/03] Step [018/025]: acc=0.5000 g_loss=0.6723 d_loss=0.6929 kd_loss=0.0018
Epoch [01/03] Step [019/025]: acc=0.5000 g_loss=0.6698 d_loss=0.6930 kd_loss=0.0030
Epoch [01/03] Step [020/025]: acc=0.5000 g_loss=0.6692 d_loss=0.6934 kd_loss=0.0035
Epoch [01/03] Step [021/025]: acc=0.5000 g_loss=0.6708 d_loss=0.6932 kd_loss=0.0056
Epoch [01/03] Step [022/025]: acc=0.5000 g_loss=0.6726 d_loss=0.6933 kd_loss=0.0069
Epoch [01/03] Step [023/025]: acc=0.5000 g_loss=0.6764 d_loss=0.6934 kd_loss=0.0083
Epoch [01/03] Step [024/025]: acc=0.5000 g_loss=0.6810 d_loss=0.6938 kd_loss=0.0070
Epoch [01/03] Step [025/025]: acc=0.5000 g_loss=0.6876 d_loss=0.6931 kd_loss=0.0047
Avg Loss = 0.6706, Avg Accuracy = 0.6040
Epoch [02/03] Step [001/025]: acc=0.5000 g_loss=0.6928 d_loss=0.6930 kd_loss=0.0002
Epoch [02/03] Step [002/025]: acc=0.5000 g_loss=0.6959 d_loss=0.6932 kd_loss=0.0010
Epoch [02/03] Step [003/025]: acc=0.5000 g_loss=0.6983 d_loss=0.6930 kd_loss=0.0021
Epoch [02/03] Step [004/025]: acc=0.5000 g_loss=0.6986 d_loss=0.6931 kd_loss=0.0011
Epoch [02/03] Step [005/025]: acc=0.5000 g_loss=0.6979 d_loss=0.6930 kd_loss=0.0003
Epoch [02/03] Step [006/025]: acc=0.5000 g_loss=0.6976 d_loss=0.6933 kd_loss=0.0005
Epoch [02/03] Step [007/025]: acc=0.5000 g_loss=0.6960 d_loss=0.6928 kd_loss=0.0008
Epoch [02/03] Step [008/025]: acc=0.5000 g_loss=0.6953 d_loss=0.6934 kd_loss=0.0013
Epoch [02/03] Step [009/025]: acc=0.5000 g_loss=0.6955 d_loss=0.6931 kd_loss=0.0012
Epoch [02/03] Step [010/025]: acc=0.5000 g_loss=0.6947 d_loss=0.6929 kd_loss=0.0015
Epoch [02/03] Step [011/025]: acc=0.5000 g_loss=0.6938 d_loss=0.6929 kd_loss=0.0017
Epoch [02/03] Step [012/025]: acc=0.5000 g_loss=0.6935 d_loss=0.6930 kd_loss=0.0013
Epoch [02/03] Step [013/025]: acc=0.5000 g_loss=0.6937 d_loss=0.6930 kd_loss=0.0005
Epoch [02/03] Step [014/025]: acc=0.5000 g_loss=0.6937 d_loss=0.6929 kd_loss=0.0001
Epoch [02/03] Step [015/025]: acc=0.5000 g_loss=0.6944 d_loss=0.6929 kd_loss=0.0005
Epoch [02/03] Step [016/025]: acc=0.5000 g_loss=0.6941 d_loss=0.6930 kd_loss=0.0007
Epoch [02/03] Step [017/025]: acc=0.5000 g_loss=0.6942 d_loss=0.6930 kd_loss=0.0007
Epoch [02/03] Step [018/025]: acc=0.5000 g_loss=0.6957 d_loss=0.6939 kd_loss=0.0007
Epoch [02/03] Step [019/025]: acc=0.5000 g_loss=0.6974 d_loss=0.6930 kd_loss=0.0001
Epoch [02/03] Step [020/025]: acc=0.5000 g_loss=0.6984 d_loss=0.6930 kd_loss=0.0001
Epoch [02/03] Step [021/025]: acc=0.5000 g_loss=0.6983 d_loss=0.6930 kd_loss=0.0001
Epoch [02/03] Step [022/025]: acc=0.5000 g_loss=0.6978 d_loss=0.6932 kd_loss=0.0002
Epoch [02/03] Step [023/025]: acc=0.5000 g_loss=0.6971 d_loss=0.6930 kd_loss=0.0001
Epoch [02/03] Step [024/025]: acc=0.5000 g_loss=0.6953 d_loss=0.6931 kd_loss=0.0001
Epoch [02/03] Step [025/025]: acc=0.5000 g_loss=0.6938 d_loss=0.6929 kd_loss=0.0003
Avg Loss = 0.6729, Avg Accuracy = 0.6040
Epoch [03/03] Step [001/025]: acc=0.5000 g_loss=0.6930 d_loss=0.6930 kd_loss=0.0004
Epoch [03/03] Step [002/025]: acc=0.5000 g_loss=0.6917 d_loss=0.6930 kd_loss=0.0002
Epoch [03/03] Step [003/025]: acc=0.5000 g_loss=0.6907 d_loss=0.6931 kd_loss=0.0001
Epoch [03/03] Step [004/025]: acc=0.5000 g_loss=0.6912 d_loss=0.6935 kd_loss=0.0003
Epoch [03/03] Step [005/025]: acc=0.5000 g_loss=0.6926 d_loss=0.6932 kd_loss=0.0007
Epoch [03/03] Step [006/025]: acc=0.5000 g_loss=0.6938 d_loss=0.6930 kd_loss=0.0008
Epoch [03/03] Step [007/025]: acc=0.5000 g_loss=0.6949 d_loss=0.6929 kd_loss=0.0007
Epoch [03/03] Step [008/025]: acc=0.5000 g_loss=0.6955 d_loss=0.6931 kd_loss=0.0004
Epoch [03/03] Step [009/025]: acc=0.5000 g_loss=0.6969 d_loss=0.6930 kd_loss=0.0002
Epoch [03/03] Step [010/025]: acc=0.5000 g_loss=0.6969 d_loss=0.6931 kd_loss=0.0001
Epoch [03/03] Step [011/025]: acc=0.5000 g_loss=0.6967 d_loss=0.6931 kd_loss=0.0001
Epoch [03/03] Step [012/025]: acc=0.5000 g_loss=0.6961 d_loss=0.6934 kd_loss=0.0001
Epoch [03/03] Step [013/025]: acc=0.5000 g_loss=0.6953 d_loss=0.6931 kd_loss=0.0002
Epoch [03/03] Step [014/025]: acc=0.5000 g_loss=0.6951 d_loss=0.6934 kd_loss=0.0004
Epoch [03/03] Step [015/025]: acc=0.5000 g_loss=0.6949 d_loss=0.6930 kd_loss=0.0003
Epoch [03/03] Step [016/025]: acc=0.5000 g_loss=0.6939 d_loss=0.6932 kd_loss=0.0002
Epoch [03/03] Step [017/025]: acc=0.5000 g_loss=0.6937 d_loss=0.6931 kd_loss=0.0002
Epoch [03/03] Step [018/025]: acc=0.5000 g_loss=0.6930 d_loss=0.6931 kd_loss=0.0002
Epoch [03/03] Step [019/025]: acc=0.5000 g_loss=0.6932 d_loss=0.6933 kd_loss=0.0002
Epoch [03/03] Step [020/025]: acc=0.5000 g_loss=0.6938 d_loss=0.6932 kd_loss=0.0003
Epoch [03/03] Step [021/025]: acc=0.5000 g_loss=0.6943 d_loss=0.6931 kd_loss=0.0001
Epoch [03/03] Step [022/025]: acc=0.5000 g_loss=0.6945 d_loss=0.6932 kd_loss=0.0001
Epoch [03/03] Step [023/025]: acc=0.5000 g_loss=0.6948 d_loss=0.6931 kd_loss=0.0000
Epoch [03/03] Step [024/025]: acc=0.5000 g_loss=0.6948 d_loss=0.6931 kd_loss=0.0001
Epoch [03/03] Step [025/025]: acc=0.5000 g_loss=0.6948 d_loss=0.6930 kd_loss=0.0001
Avg Loss = 0.6722, Avg Accuracy = 0.6040
=== Evaluating classifier for encoded target domain ===
>>> source only <<<

