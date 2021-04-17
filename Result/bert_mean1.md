~~~
=== Argument Setting ===
src: news
tgt: community
seed: 42
train_seed: 42
model_type: bert
max_seq_length: 128
batch_size: 32
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
Epoch [01/03] Step [001/050]: cls_loss=0.7303
Epoch [01/03] Step [002/050]: cls_loss=0.7221
Epoch [01/03] Step [003/050]: cls_loss=0.6739
Epoch [01/03] Step [004/050]: cls_loss=0.6860
Epoch [01/03] Step [005/050]: cls_loss=0.6471
Epoch [01/03] Step [006/050]: cls_loss=0.7414
Epoch [01/03] Step [007/050]: cls_loss=0.6722
Epoch [01/03] Step [008/050]: cls_loss=0.6671
Epoch [01/03] Step [009/050]: cls_loss=0.6390
Epoch [01/03] Step [010/050]: cls_loss=0.6163
Epoch [01/03] Step [011/050]: cls_loss=0.6043
Epoch [01/03] Step [012/050]: cls_loss=0.6535
Epoch [01/03] Step [013/050]: cls_loss=0.7218
Epoch [01/03] Step [014/050]: cls_loss=0.5872
Epoch [01/03] Step [015/050]: cls_loss=0.7190
Epoch [01/03] Step [016/050]: cls_loss=0.7907
Epoch [01/03] Step [017/050]: cls_loss=0.6641
Epoch [01/03] Step [018/050]: cls_loss=0.6961
Epoch [01/03] Step [019/050]: cls_loss=0.6609
Epoch [01/03] Step [020/050]: cls_loss=0.6670
Epoch [01/03] Step [021/050]: cls_loss=0.6744
Epoch [01/03] Step [022/050]: cls_loss=0.6797
Epoch [01/03] Step [023/050]: cls_loss=0.7479
Epoch [01/03] Step [024/050]: cls_loss=0.6836
Epoch [01/03] Step [025/050]: cls_loss=0.7182
Epoch [01/03] Step [026/050]: cls_loss=0.7158
Epoch [01/03] Step [027/050]: cls_loss=0.7469
Epoch [01/03] Step [028/050]: cls_loss=0.6724
Epoch [01/03] Step [029/050]: cls_loss=0.6464
Epoch [01/03] Step [030/050]: cls_loss=0.6776
Epoch [01/03] Step [031/050]: cls_loss=0.6627
Epoch [01/03] Step [032/050]: cls_loss=0.6835
Epoch [01/03] Step [033/050]: cls_loss=0.6566
Epoch [01/03] Step [034/050]: cls_loss=0.6926
Epoch [01/03] Step [035/050]: cls_loss=0.6931
Epoch [01/03] Step [036/050]: cls_loss=0.6642
Epoch [01/03] Step [037/050]: cls_loss=0.6332
Epoch [01/03] Step [038/050]: cls_loss=0.6461
Epoch [01/03] Step [039/050]: cls_loss=0.6976
Epoch [01/03] Step [040/050]: cls_loss=0.6773
Epoch [01/03] Step [041/050]: cls_loss=0.5756
Epoch [01/03] Step [042/050]: cls_loss=0.6890
Epoch [01/03] Step [043/050]: cls_loss=0.6927
Epoch [01/03] Step [044/050]: cls_loss=0.7706
Epoch [01/03] Step [045/050]: cls_loss=0.7353
Epoch [01/03] Step [046/050]: cls_loss=0.6715
Epoch [01/03] Step [047/050]: cls_loss=0.6729
Epoch [01/03] Step [048/050]: cls_loss=0.6448
Epoch [01/03] Step [049/050]: cls_loss=0.7034
Epoch [01/03] Step [050/050]: cls_loss=0.6643
Epoch [02/03] Step [001/050]: cls_loss=0.6886
Epoch [02/03] Step [002/050]: cls_loss=0.6167
Epoch [02/03] Step [003/050]: cls_loss=0.6641
Epoch [02/03] Step [004/050]: cls_loss=0.6389
Epoch [02/03] Step [005/050]: cls_loss=0.6517
Epoch [02/03] Step [006/050]: cls_loss=0.5777
Epoch [02/03] Step [007/050]: cls_loss=0.5858
Epoch [02/03] Step [008/050]: cls_loss=0.6031
Epoch [02/03] Step [009/050]: cls_loss=0.5956
Epoch [02/03] Step [010/050]: cls_loss=0.5594
Epoch [02/03] Step [011/050]: cls_loss=0.6076
Epoch [02/03] Step [012/050]: cls_loss=0.8576
Epoch [02/03] Step [013/050]: cls_loss=0.6187
Epoch [02/03] Step [014/050]: cls_loss=0.6291
Epoch [02/03] Step [015/050]: cls_loss=0.5709
Epoch [02/03] Step [016/050]: cls_loss=0.7052
Epoch [02/03] Step [017/050]: cls_loss=0.5685
Epoch [02/03] Step [018/050]: cls_loss=0.6939
Epoch [02/03] Step [019/050]: cls_loss=0.5898
Epoch [02/03] Step [020/050]: cls_loss=0.7066
Epoch [02/03] Step [021/050]: cls_loss=0.6192
Epoch [02/03] Step [022/050]: cls_loss=0.7278
Epoch [02/03] Step [023/050]: cls_loss=0.6483
Epoch [02/03] Step [024/050]: cls_loss=0.5796
Epoch [02/03] Step [025/050]: cls_loss=0.6798
Epoch [02/03] Step [026/050]: cls_loss=0.6535
Epoch [02/03] Step [027/050]: cls_loss=0.6778
Epoch [02/03] Step [028/050]: cls_loss=0.6454
Epoch [02/03] Step [029/050]: cls_loss=0.6192
Epoch [02/03] Step [030/050]: cls_loss=0.6824
Epoch [02/03] Step [031/050]: cls_loss=0.7071
Epoch [02/03] Step [032/050]: cls_loss=0.6763
Epoch [02/03] Step [033/050]: cls_loss=0.9051
Epoch [02/03] Step [034/050]: cls_loss=0.7271
Epoch [02/03] Step [035/050]: cls_loss=0.6307
Epoch [02/03] Step [036/050]: cls_loss=0.6089
Epoch [02/03] Step [037/050]: cls_loss=0.6226
Epoch [02/03] Step [038/050]: cls_loss=0.6805
Epoch [02/03] Step [039/050]: cls_loss=0.6349
Epoch [02/03] Step [040/050]: cls_loss=0.6017
Epoch [02/03] Step [041/050]: cls_loss=0.5921
Epoch [02/03] Step [042/050]: cls_loss=0.5468
Epoch [02/03] Step [043/050]: cls_loss=0.6176
Epoch [02/03] Step [044/050]: cls_loss=0.5970
Epoch [02/03] Step [045/050]: cls_loss=0.6889
Epoch [02/03] Step [046/050]: cls_loss=0.6534
Epoch [02/03] Step [047/050]: cls_loss=0.6296
Epoch [02/03] Step [048/050]: cls_loss=0.6465
Epoch [02/03] Step [049/050]: cls_loss=0.6278
Epoch [02/03] Step [050/050]: cls_loss=0.6463
Epoch [03/03] Step [001/050]: cls_loss=0.6330
Epoch [03/03] Step [002/050]: cls_loss=0.6108
Epoch [03/03] Step [003/050]: cls_loss=0.6595
Epoch [03/03] Step [004/050]: cls_loss=0.5238
Epoch [03/03] Step [005/050]: cls_loss=0.5540
Epoch [03/03] Step [006/050]: cls_loss=0.5732
Epoch [03/03] Step [007/050]: cls_loss=0.5249
Epoch [03/03] Step [008/050]: cls_loss=0.4018
Epoch [03/03] Step [009/050]: cls_loss=0.7938
Epoch [03/03] Step [010/050]: cls_loss=0.6714
Epoch [03/03] Step [011/050]: cls_loss=0.6244
Epoch [03/03] Step [012/050]: cls_loss=0.7182
Epoch [03/03] Step [013/050]: cls_loss=0.8382
Epoch [03/03] Step [014/050]: cls_loss=0.6584
Epoch [03/03] Step [015/050]: cls_loss=0.6647
Epoch [03/03] Step [016/050]: cls_loss=0.6381
Epoch [03/03] Step [017/050]: cls_loss=0.6351
Epoch [03/03] Step [018/050]: cls_loss=0.6223
Epoch [03/03] Step [019/050]: cls_loss=0.6454
Epoch [03/03] Step [020/050]: cls_loss=0.6389
Epoch [03/03] Step [021/050]: cls_loss=0.5962
Epoch [03/03] Step [022/050]: cls_loss=0.5844
Epoch [03/03] Step [023/050]: cls_loss=0.6431
Epoch [03/03] Step [024/050]: cls_loss=0.7154
Epoch [03/03] Step [025/050]: cls_loss=0.6586
Epoch [03/03] Step [026/050]: cls_loss=0.8184
Epoch [03/03] Step [027/050]: cls_loss=0.6739
Epoch [03/03] Step [028/050]: cls_loss=0.5692
Epoch [03/03] Step [029/050]: cls_loss=0.5601
Epoch [03/03] Step [030/050]: cls_loss=0.5208
Epoch [03/03] Step [031/050]: cls_loss=0.6124
Epoch [03/03] Step [032/050]: cls_loss=0.5688
Epoch [03/03] Step [033/050]: cls_loss=0.5532
Epoch [03/03] Step [034/050]: cls_loss=0.4977
Epoch [03/03] Step [035/050]: cls_loss=0.5531
Epoch [03/03] Step [036/050]: cls_loss=0.6381
Epoch [03/03] Step [037/050]: cls_loss=0.6851
Epoch [03/03] Step [038/050]: cls_loss=0.5280
Epoch [03/03] Step [039/050]: cls_loss=0.6897
Epoch [03/03] Step [040/050]: cls_loss=0.3971
Epoch [03/03] Step [041/050]: cls_loss=0.6668
Epoch [03/03] Step [042/050]: cls_loss=0.6478
Epoch [03/03] Step [043/050]: cls_loss=0.4768
Epoch [03/03] Step [044/050]: cls_loss=0.5772
Epoch [03/03] Step [045/050]: cls_loss=0.6964
Epoch [03/03] Step [046/050]: cls_loss=0.4850
Epoch [03/03] Step [047/050]: cls_loss=0.5837
Epoch [03/03] Step [048/050]: cls_loss=0.7570
Epoch [03/03] Step [049/050]: cls_loss=0.5801
Epoch [03/03] Step [050/050]: cls_loss=0.6264
save pretrained model to: /content/snapshots/news/bert/42/source-encoder.pt
save pretrained model to: /content/snapshots/news/bert/42/source-classifier.pt
=== Evaluating classifier for source domain ===
Avg Loss = 0.5885, Avg Accuracy = 0.7281
Avg Loss = 0.6471, Avg Accuracy = 0.6175
Avg Loss = 0.6371, Avg Accuracy = 0.6670
=== Training encoder for target domain ===
Epoch [01/03] Step [001/050]: acc=0.5000 g_loss=0.6865 d_loss=0.6943 kd_loss=0.0020
Epoch [01/03] Step [002/050]: acc=0.5000 g_loss=0.6849 d_loss=0.6933 kd_loss=0.0019
Epoch [01/03] Step [003/050]: acc=0.5000 g_loss=0.6854 d_loss=0.6926 kd_loss=0.0024
Epoch [01/03] Step [004/050]: acc=0.5000 g_loss=0.6831 d_loss=0.6936 kd_loss=0.0013
Epoch [01/03] Step [005/050]: acc=0.5000 g_loss=0.6840 d_loss=0.6928 kd_loss=0.0045
Epoch [01/03] Step [006/050]: acc=0.5000 g_loss=0.6839 d_loss=0.6933 kd_loss=0.0014
Epoch [01/03] Step [007/050]: acc=0.5000 g_loss=0.6835 d_loss=0.6929 kd_loss=0.0015
Epoch [01/03] Step [008/050]: acc=0.5000 g_loss=0.6844 d_loss=0.6922 kd_loss=0.0028
Epoch [01/03] Step [009/050]: acc=0.5000 g_loss=0.6843 d_loss=0.6924 kd_loss=0.0035
Epoch [01/03] Step [010/050]: acc=0.5000 g_loss=0.6837 d_loss=0.6927 kd_loss=0.0047
Epoch [01/03] Step [011/050]: acc=0.5000 g_loss=0.6805 d_loss=0.6959 kd_loss=0.0023
Epoch [01/03] Step [012/050]: acc=0.5000 g_loss=0.6815 d_loss=0.6915 kd_loss=0.0042
Epoch [01/03] Step [013/050]: acc=0.5000 g_loss=0.6784 d_loss=0.6940 kd_loss=0.0023
Epoch [01/03] Step [014/050]: acc=0.5000 g_loss=0.6794 d_loss=0.6951 kd_loss=0.0032
Epoch [01/03] Step [015/050]: acc=0.5000 g_loss=0.6799 d_loss=0.6921 kd_loss=0.0040
Epoch [01/03] Step [016/050]: acc=0.5000 g_loss=0.6798 d_loss=0.6927 kd_loss=0.0057
Epoch [01/03] Step [017/050]: acc=0.5000 g_loss=0.6790 d_loss=0.6938 kd_loss=0.0075
Epoch [01/03] Step [018/050]: acc=0.5000 g_loss=0.6777 d_loss=0.6932 kd_loss=0.0046
Epoch [01/03] Step [019/050]: acc=0.5000 g_loss=0.6774 d_loss=0.6938 kd_loss=0.0025
Epoch [01/03] Step [020/050]: acc=0.5000 g_loss=0.6776 d_loss=0.6939 kd_loss=0.0024
Epoch [01/03] Step [021/050]: acc=0.5000 g_loss=0.6779 d_loss=0.6930 kd_loss=0.0044
Epoch [01/03] Step [022/050]: acc=0.5000 g_loss=0.6770 d_loss=0.6937 kd_loss=0.0036
Epoch [01/03] Step [023/050]: acc=0.5000 g_loss=0.6765 d_loss=0.6934 kd_loss=0.0024
Epoch [01/03] Step [024/050]: acc=0.5000 g_loss=0.6755 d_loss=0.6930 kd_loss=0.0041
Epoch [01/03] Step [025/050]: acc=0.5000 g_loss=0.6756 d_loss=0.6931 kd_loss=0.0037
Epoch [01/03] Step [026/050]: acc=0.5000 g_loss=0.6739 d_loss=0.6932 kd_loss=0.0040
Epoch [01/03] Step [027/050]: acc=0.5000 g_loss=0.6721 d_loss=0.6943 kd_loss=0.0041
Epoch [01/03] Step [028/050]: acc=0.5000 g_loss=0.6729 d_loss=0.6929 kd_loss=0.0016
Epoch [01/03] Step [029/050]: acc=0.5000 g_loss=0.6720 d_loss=0.6929 kd_loss=0.0031
Epoch [01/03] Step [030/050]: acc=0.5000 g_loss=0.6710 d_loss=0.6926 kd_loss=0.0037
Epoch [01/03] Step [031/050]: acc=0.5000 g_loss=0.6704 d_loss=0.6928 kd_loss=0.0022
Epoch [01/03] Step [032/050]: acc=0.5000 g_loss=0.6690 d_loss=0.6945 kd_loss=0.0023
Epoch [01/03] Step [033/050]: acc=0.5000 g_loss=0.6689 d_loss=0.6940 kd_loss=0.0049
Epoch [01/03] Step [034/050]: acc=0.5000 g_loss=0.6702 d_loss=0.6927 kd_loss=0.0055
Epoch [01/03] Step [035/050]: acc=0.5000 g_loss=0.6706 d_loss=0.6931 kd_loss=0.0039
Epoch [01/03] Step [036/050]: acc=0.5000 g_loss=0.6740 d_loss=0.6915 kd_loss=0.0025
Epoch [01/03] Step [037/050]: acc=0.5000 g_loss=0.6719 d_loss=0.6919 kd_loss=0.0047
Epoch [01/03] Step [038/050]: acc=0.5000 g_loss=0.6670 d_loss=0.6933 kd_loss=0.0058
Epoch [01/03] Step [039/050]: acc=0.5000 g_loss=0.6684 d_loss=0.6929 kd_loss=0.0051
Epoch [01/03] Step [040/050]: acc=0.5000 g_loss=0.6698 d_loss=0.6934 kd_loss=0.0039
Epoch [01/03] Step [041/050]: acc=0.5000 g_loss=0.6729 d_loss=0.6929 kd_loss=0.0027
Epoch [01/03] Step [042/050]: acc=0.5000 g_loss=0.6748 d_loss=0.6933 kd_loss=0.0047
Epoch [01/03] Step [043/050]: acc=0.5000 g_loss=0.6768 d_loss=0.6932 kd_loss=0.0058
Epoch [01/03] Step [044/050]: acc=0.5000 g_loss=0.6778 d_loss=0.6928 kd_loss=0.0087
Epoch [01/03] Step [045/050]: acc=0.5000 g_loss=0.6783 d_loss=0.6938 kd_loss=0.0063
Epoch [01/03] Step [046/050]: acc=0.5000 g_loss=0.6820 d_loss=0.6924 kd_loss=0.0028
Epoch [01/03] Step [047/050]: acc=0.5000 g_loss=0.6824 d_loss=0.6925 kd_loss=0.0035
Epoch [01/03] Step [048/050]: acc=0.5000 g_loss=0.6805 d_loss=0.6934 kd_loss=0.0036
Epoch [01/03] Step [049/050]: acc=0.5000 g_loss=0.6806 d_loss=0.6935 kd_loss=0.0046
Epoch [01/03] Step [050/050]: acc=0.5000 g_loss=0.6785 d_loss=0.6931 kd_loss=0.0077
Avg Loss = 0.6347, Avg Accuracy = 0.6790
Epoch [02/03] Step [001/050]: acc=0.5000 g_loss=0.6756 d_loss=0.6940 kd_loss=0.0029
Epoch [02/03] Step [002/050]: acc=0.5000 g_loss=0.6747 d_loss=0.6937 kd_loss=0.0030
Epoch [02/03] Step [003/050]: acc=0.5000 g_loss=0.6745 d_loss=0.6940 kd_loss=0.0029
Epoch [02/03] Step [004/050]: acc=0.5000 g_loss=0.6757 d_loss=0.6931 kd_loss=0.0017
Epoch [02/03] Step [005/050]: acc=0.5000 g_loss=0.6779 d_loss=0.6941 kd_loss=0.0042
Epoch [02/03] Step [006/050]: acc=0.5000 g_loss=0.6814 d_loss=0.6929 kd_loss=0.0022
Epoch [02/03] Step [007/050]: acc=0.5000 g_loss=0.6851 d_loss=0.6932 kd_loss=0.0020
Epoch [02/03] Step [008/050]: acc=0.5000 g_loss=0.6891 d_loss=0.6927 kd_loss=0.0032
Epoch [02/03] Step [009/050]: acc=0.5000 g_loss=0.6902 d_loss=0.6939 kd_loss=0.0066
Epoch [02/03] Step [010/050]: acc=0.5000 g_loss=0.6901 d_loss=0.6936 kd_loss=0.0026
Epoch [02/03] Step [011/050]: acc=0.5000 g_loss=0.6894 d_loss=0.6934 kd_loss=0.0028
Epoch [02/03] Step [012/050]: acc=0.5000 g_loss=0.6880 d_loss=0.6930 kd_loss=0.0025
Epoch [02/03] Step [013/050]: acc=0.5000 g_loss=0.6847 d_loss=0.6930 kd_loss=0.0024
Epoch [02/03] Step [014/050]: acc=0.5000 g_loss=0.6820 d_loss=0.6930 kd_loss=0.0033
Epoch [02/03] Step [015/050]: acc=0.5000 g_loss=0.6822 d_loss=0.6932 kd_loss=0.0058
Epoch [02/03] Step [016/050]: acc=0.5000 g_loss=0.6825 d_loss=0.6930 kd_loss=0.0029
Epoch [02/03] Step [017/050]: acc=0.5000 g_loss=0.6800 d_loss=0.6929 kd_loss=0.0024
Epoch [02/03] Step [018/050]: acc=0.5000 g_loss=0.6823 d_loss=0.6942 kd_loss=0.0069
Epoch [02/03] Step [019/050]: acc=0.5000 g_loss=0.6858 d_loss=0.6929 kd_loss=0.0055
Epoch [02/03] Step [020/050]: acc=0.5000 g_loss=0.6888 d_loss=0.6925 kd_loss=0.0044
Epoch [02/03] Step [021/050]: acc=0.5000 g_loss=0.6896 d_loss=0.6929 kd_loss=0.0038
Epoch [02/03] Step [022/050]: acc=0.5000 g_loss=0.6901 d_loss=0.6938 kd_loss=0.0018
Epoch [02/03] Step [023/050]: acc=0.5000 g_loss=0.6910 d_loss=0.6924 kd_loss=0.0022
Epoch [02/03] Step [024/050]: acc=0.5000 g_loss=0.6914 d_loss=0.6920 kd_loss=0.0036
Epoch [02/03] Step [025/050]: acc=0.5000 g_loss=0.6843 d_loss=0.6935 kd_loss=0.0028
Epoch [02/03] Step [026/050]: acc=0.5000 g_loss=0.6838 d_loss=0.6927 kd_loss=0.0030
Epoch [02/03] Step [027/050]: acc=0.5000 g_loss=0.6828 d_loss=0.6938 kd_loss=0.0028
Epoch [02/03] Step [028/050]: acc=0.5000 g_loss=0.6835 d_loss=0.6933 kd_loss=0.0029
Epoch [02/03] Step [029/050]: acc=0.5000 g_loss=0.6845 d_loss=0.6937 kd_loss=0.0021
Epoch [02/03] Step [030/050]: acc=0.5000 g_loss=0.6829 d_loss=0.6934 kd_loss=0.0028
Epoch [02/03] Step [031/050]: acc=0.5000 g_loss=0.6835 d_loss=0.6929 kd_loss=0.0021
Epoch [02/03] Step [032/050]: acc=0.5000 g_loss=0.6830 d_loss=0.6926 kd_loss=0.0024
Epoch [02/03] Step [033/050]: acc=0.5000 g_loss=0.6815 d_loss=0.6931 kd_loss=0.0026
Epoch [02/03] Step [034/050]: acc=0.5000 g_loss=0.6807 d_loss=0.6937 kd_loss=0.0021
Epoch [02/03] Step [035/050]: acc=0.5000 g_loss=0.6814 d_loss=0.6927 kd_loss=0.0036
Epoch [02/03] Step [036/050]: acc=0.5000 g_loss=0.6792 d_loss=0.6933 kd_loss=0.0028
Epoch [02/03] Step [037/050]: acc=0.5000 g_loss=0.6794 d_loss=0.6929 kd_loss=0.0021
Epoch [02/03] Step [038/050]: acc=0.5000 g_loss=0.6780 d_loss=0.6934 kd_loss=0.0021
Epoch [02/03] Step [039/050]: acc=0.5000 g_loss=0.6776 d_loss=0.6924 kd_loss=0.0018
Epoch [02/03] Step [040/050]: acc=0.5000 g_loss=0.6770 d_loss=0.6914 kd_loss=0.0031
Epoch [02/03] Step [041/050]: acc=0.5000 g_loss=0.6718 d_loss=0.6934 kd_loss=0.0022
Epoch [02/03] Step [042/050]: acc=0.5000 g_loss=0.6688 d_loss=0.6941 kd_loss=0.0022
Epoch [02/03] Step [043/050]: acc=0.5000 g_loss=0.6690 d_loss=0.6933 kd_loss=0.0032
Epoch [02/03] Step [044/050]: acc=0.5000 g_loss=0.6685 d_loss=0.6932 kd_loss=0.0034
Epoch [02/03] Step [045/050]: acc=0.5000 g_loss=0.6690 d_loss=0.6928 kd_loss=0.0023
Epoch [02/03] Step [046/050]: acc=0.5000 g_loss=0.6692 d_loss=0.6936 kd_loss=0.0026
Epoch [02/03] Step [047/050]: acc=0.5000 g_loss=0.6706 d_loss=0.6934 kd_loss=0.0035
Epoch [02/03] Step [048/050]: acc=0.5000 g_loss=0.6747 d_loss=0.6931 kd_loss=0.0049
Epoch [02/03] Step [049/050]: acc=0.5000 g_loss=0.6757 d_loss=0.6931 kd_loss=0.0024
Epoch [02/03] Step [050/050]: acc=0.5000 g_loss=0.6779 d_loss=0.6937 kd_loss=0.0018
Avg Loss = 0.6496, Avg Accuracy = 0.6600
Epoch [03/03] Step [001/050]: acc=0.5000 g_loss=0.6817 d_loss=0.6925 kd_loss=0.0048
Epoch [03/03] Step [002/050]: acc=0.5000 g_loss=0.6848 d_loss=0.6930 kd_loss=0.0035
Epoch [03/03] Step [003/050]: acc=0.5000 g_loss=0.6858 d_loss=0.6935 kd_loss=0.0017
Epoch [03/03] Step [004/050]: acc=0.5000 g_loss=0.6901 d_loss=0.6931 kd_loss=0.0018
Epoch [03/03] Step [005/050]: acc=0.5000 g_loss=0.6918 d_loss=0.6931 kd_loss=0.0023
Epoch [03/03] Step [006/050]: acc=0.5000 g_loss=0.6923 d_loss=0.6931 kd_loss=0.0021
Epoch [03/03] Step [007/050]: acc=0.5000 g_loss=0.6932 d_loss=0.6940 kd_loss=0.0009
Epoch [03/03] Step [008/050]: acc=0.5000 g_loss=0.6943 d_loss=0.6931 kd_loss=0.0023
Epoch [03/03] Step [009/050]: acc=0.5000 g_loss=0.6955 d_loss=0.6931 kd_loss=0.0028
Epoch [03/03] Step [010/050]: acc=0.5000 g_loss=0.6963 d_loss=0.6932 kd_loss=0.0024
Epoch [03/03] Step [011/050]: acc=0.5000 g_loss=0.6971 d_loss=0.6930 kd_loss=0.0017
Epoch [03/03] Step [012/050]: acc=0.5000 g_loss=0.6968 d_loss=0.6929 kd_loss=0.0022
Epoch [03/03] Step [013/050]: acc=0.5000 g_loss=0.6960 d_loss=0.6931 kd_loss=0.0012
Epoch [03/03] Step [014/050]: acc=0.5000 g_loss=0.6959 d_loss=0.6931 kd_loss=0.0014
Epoch [03/03] Step [015/050]: acc=0.5000 g_loss=0.6957 d_loss=0.6932 kd_loss=0.0012
Epoch [03/03] Step [016/050]: acc=0.5000 g_loss=0.6947 d_loss=0.6929 kd_loss=0.0032
Epoch [03/03] Step [017/050]: acc=0.5000 g_loss=0.6943 d_loss=0.6934 kd_loss=0.0012
Epoch [03/03] Step [018/050]: acc=0.5000 g_loss=0.6954 d_loss=0.6927 kd_loss=0.0010
Epoch [03/03] Step [019/050]: acc=0.5000 g_loss=0.6933 d_loss=0.6927 kd_loss=0.0016
Epoch [03/03] Step [020/050]: acc=0.5000 g_loss=0.6922 d_loss=0.6931 kd_loss=0.0008
Epoch [03/03] Step [021/050]: acc=0.5000 g_loss=0.6917 d_loss=0.6930 kd_loss=0.0025
Epoch [03/03] Step [022/050]: acc=0.5000 g_loss=0.6894 d_loss=0.6936 kd_loss=0.0015
Epoch [03/03] Step [023/050]: acc=0.5000 g_loss=0.6888 d_loss=0.6930 kd_loss=0.0015
Epoch [03/03] Step [024/050]: acc=0.5000 g_loss=0.6891 d_loss=0.6932 kd_loss=0.0024
Epoch [03/03] Step [025/050]: acc=0.5000 g_loss=0.6885 d_loss=0.6929 kd_loss=0.0012
Epoch [03/03] Step [026/050]: acc=0.5000 g_loss=0.6876 d_loss=0.6932 kd_loss=0.0019
Epoch [03/03] Step [027/050]: acc=0.5000 g_loss=0.6890 d_loss=0.6930 kd_loss=0.0013
Epoch [03/03] Step [028/050]: acc=0.5000 g_loss=0.6877 d_loss=0.6931 kd_loss=0.0018
Epoch [03/03] Step [029/050]: acc=0.5000 g_loss=0.6878 d_loss=0.6931 kd_loss=0.0022
Epoch [03/03] Step [030/050]: acc=0.5000 g_loss=0.6878 d_loss=0.6933 kd_loss=0.0011
Epoch [03/03] Step [031/050]: acc=0.5000 g_loss=0.6882 d_loss=0.6926 kd_loss=0.0010
Epoch [03/03] Step [032/050]: acc=0.5000 g_loss=0.6862 d_loss=0.6937 kd_loss=0.0017
Epoch [03/03] Step [033/050]: acc=0.5000 g_loss=0.6872 d_loss=0.6932 kd_loss=0.0020
Epoch [03/03] Step [034/050]: acc=0.5000 g_loss=0.6866 d_loss=0.6935 kd_loss=0.0015
Epoch [03/03] Step [035/050]: acc=0.5000 g_loss=0.6877 d_loss=0.6929 kd_loss=0.0010
Epoch [03/03] Step [036/050]: acc=0.5000 g_loss=0.6884 d_loss=0.6935 kd_loss=0.0010
Epoch [03/03] Step [037/050]: acc=0.5000 g_loss=0.6885 d_loss=0.6933 kd_loss=0.0015
Epoch [03/03] Step [038/050]: acc=0.5000 g_loss=0.6886 d_loss=0.6932 kd_loss=0.0021
Epoch [03/03] Step [039/050]: acc=0.5000 g_loss=0.6888 d_loss=0.6936 kd_loss=0.0012
Epoch [03/03] Step [040/050]: acc=0.5000 g_loss=0.6892 d_loss=0.6932 kd_loss=0.0012
Epoch [03/03] Step [041/050]: acc=0.5000 g_loss=0.6893 d_loss=0.6931 kd_loss=0.0011
Epoch [03/03] Step [042/050]: acc=0.5000 g_loss=0.6894 d_loss=0.6931 kd_loss=0.0011
Epoch [03/03] Step [043/050]: acc=0.5000 g_loss=0.6898 d_loss=0.6930 kd_loss=0.0013
Epoch [03/03] Step [044/050]: acc=0.5000 g_loss=0.6896 d_loss=0.6932 kd_loss=0.0011
Epoch [03/03] Step [045/050]: acc=0.5000 g_loss=0.6892 d_loss=0.6933 kd_loss=0.0005
Epoch [03/03] Step [046/050]: acc=0.5000 g_loss=0.6898 d_loss=0.6933 kd_loss=0.0015
Epoch [03/03] Step [047/050]: acc=0.5000 g_loss=0.6901 d_loss=0.6935 kd_loss=0.0015
Epoch [03/03] Step [048/050]: acc=0.5000 g_loss=0.6906 d_loss=0.6933 kd_loss=0.0011
Epoch [03/03] Step [049/050]: acc=0.5000 g_loss=0.6911 d_loss=0.6932 kd_loss=0.0013
Epoch [03/03] Step [050/050]: acc=0.5000 g_loss=0.6915 d_loss=0.6933 kd_loss=0.0011
Avg Loss = 0.6357, Avg Accuracy = 0.6675
=== Evaluating classifier for encoded target domain ===
>>> source only <<<
Avg Loss = 0.6369, Avg Accuracy = 0.6670
>>> domain adaption <<<
Avg Loss = 0.6365, Avg Accuracy = 0.6675
~~~
