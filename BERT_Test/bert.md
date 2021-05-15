2021-05-15 08:24:48.118483: I tensorflow/stream_executor/platform/default/dso_loader.cc:49] Successfully opened dynamic library libcudart.so.11.0
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
Some weights of the model checkpoint at bert-base-multilingual-cased were not used when initializing BertModel: ['cls.predictions.decoder.weight', 'cls.seq_relationship.bias', 'cls.predictions.transform.dense.weight', 'cls.predictions.transform.dense.bias', 'cls.predictions.bias', 'cls.seq_relationship.weight', 'cls.predictions.transform.LayerNorm.bias', 'cls.predictions.transform.LayerNorm.weight']
- This IS expected if you are initializing BertModel from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).
- This IS NOT expected if you are initializing BertModel from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).
Some weights of the model checkpoint at bert-base-multilingual-cased were not used when initializing BertModel: ['cls.predictions.decoder.weight', 'cls.seq_relationship.bias', 'cls.predictions.transform.dense.weight', 'cls.predictions.transform.dense.bias', 'cls.predictions.bias', 'cls.seq_relationship.weight', 'cls.predictions.transform.LayerNorm.bias', 'cls.predictions.transform.LayerNorm.weight']
- This IS expected if you are initializing BertModel from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).
- This IS NOT expected if you are initializing BertModel from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).
=== Training classifier for source domain ===
Epoch [01/03] Step [001/025]: cls_loss=0.7082
Epoch [01/03] Step [002/025]: cls_loss=0.6437
Epoch [01/03] Step [003/025]: cls_loss=0.7876
Epoch [01/03] Step [004/025]: cls_loss=0.7011
Epoch [01/03] Step [005/025]: cls_loss=0.6699
Epoch [01/03] Step [006/025]: cls_loss=0.6910
Epoch [01/03] Step [007/025]: cls_loss=0.6752
Epoch [01/03] Step [008/025]: cls_loss=0.7077
Epoch [01/03] Step [009/025]: cls_loss=0.6696
Epoch [01/03] Step [010/025]: cls_loss=0.7031
Epoch [01/03] Step [011/025]: cls_loss=0.6717
Epoch [01/03] Step [012/025]: cls_loss=0.6909
Epoch [01/03] Step [013/025]: cls_loss=0.6643
Epoch [01/03] Step [014/025]: cls_loss=0.7040
Epoch [01/03] Step [015/025]: cls_loss=0.6878
Epoch [01/03] Step [016/025]: cls_loss=0.6793
Epoch [01/03] Step [017/025]: cls_loss=0.6290
Epoch [01/03] Step [018/025]: cls_loss=0.6797
Epoch [01/03] Step [019/025]: cls_loss=0.6082
Epoch [01/03] Step [020/025]: cls_loss=0.6684
Epoch [01/03] Step [021/025]: cls_loss=0.6831
Epoch [01/03] Step [022/025]: cls_loss=0.6557
Epoch [01/03] Step [023/025]: cls_loss=0.7164
Epoch [01/03] Step [024/025]: cls_loss=0.6853
Epoch [01/03] Step [025/025]: cls_loss=0.5951
Epoch [02/03] Step [001/025]: cls_loss=0.7329
Epoch [02/03] Step [002/025]: cls_loss=0.6001
Epoch [02/03] Step [003/025]: cls_loss=0.6809
Epoch [02/03] Step [004/025]: cls_loss=0.6376
Epoch [02/03] Step [005/025]: cls_loss=0.6028
Epoch [02/03] Step [006/025]: cls_loss=0.6592
Epoch [02/03] Step [007/025]: cls_loss=0.6749
Epoch [02/03] Step [008/025]: cls_loss=0.5644
Epoch [02/03] Step [009/025]: cls_loss=0.6469
Epoch [02/03] Step [010/025]: cls_loss=0.7132
Epoch [02/03] Step [011/025]: cls_loss=0.5507
Epoch [02/03] Step [012/025]: cls_loss=0.5827
Epoch [02/03] Step [013/025]: cls_loss=0.5848
Epoch [02/03] Step [014/025]: cls_loss=0.5898
Epoch [02/03] Step [015/025]: cls_loss=0.5513
Epoch [02/03] Step [016/025]: cls_loss=0.3993
Epoch [02/03] Step [017/025]: cls_loss=0.6914
Epoch [02/03] Step [018/025]: cls_loss=0.4905
Epoch [02/03] Step [019/025]: cls_loss=0.6301
Epoch [02/03] Step [020/025]: cls_loss=0.5366
Epoch [02/03] Step [021/025]: cls_loss=0.5932
Epoch [02/03] Step [022/025]: cls_loss=0.5364
Epoch [02/03] Step [023/025]: cls_loss=0.5150
Epoch [02/03] Step [024/025]: cls_loss=0.3872
Epoch [02/03] Step [025/025]: cls_loss=0.6693
Epoch [03/03] Step [001/025]: cls_loss=0.5243
Epoch [03/03] Step [002/025]: cls_loss=0.4421
Epoch [03/03] Step [003/025]: cls_loss=0.4596
Epoch [03/03] Step [004/025]: cls_loss=0.4969
Epoch [03/03] Step [005/025]: cls_loss=0.4404
Epoch [03/03] Step [006/025]: cls_loss=0.2888
Epoch [03/03] Step [007/025]: cls_loss=0.4980
Epoch [03/03] Step [008/025]: cls_loss=0.5105
Epoch [03/03] Step [009/025]: cls_loss=0.2691
Epoch [03/03] Step [010/025]: cls_loss=0.3509
Epoch [03/03] Step [011/025]: cls_loss=0.4777
Epoch [03/03] Step [012/025]: cls_loss=0.2508
Epoch [03/03] Step [013/025]: cls_loss=0.2584
Epoch [03/03] Step [014/025]: cls_loss=0.1501
Epoch [03/03] Step [015/025]: cls_loss=0.3175
Epoch [03/03] Step [016/025]: cls_loss=0.3532
Epoch [03/03] Step [017/025]: cls_loss=0.2909
Epoch [03/03] Step [018/025]: cls_loss=0.3435
Epoch [03/03] Step [019/025]: cls_loss=0.4574
Epoch [03/03] Step [020/025]: cls_loss=0.3632
Epoch [03/03] Step [021/025]: cls_loss=0.4267
Epoch [03/03] Step [022/025]: cls_loss=0.3574
Epoch [03/03] Step [023/025]: cls_loss=0.2363
Epoch [03/03] Step [024/025]: cls_loss=0.2829
Epoch [03/03] Step [025/025]: cls_loss=0.4411
save pretrained model to: /content/snapshots/news/bert/42/source-encoder.pt
save pretrained model to: /content/snapshots/news/bert/42/source-classifier.pt
=== Evaluating classifier for source domain ===
Avg Loss = 0.1494, Avg Accuracy = 0.9513
Avg Loss = 0.4356, Avg Accuracy = 0.8100
Avg Loss = 1.0155, Avg Accuracy = 0.5820
=== Training encoder for target domain ===
Epoch [01/03] Step [001/025]: acc=0.5000 g_loss=0.6949 d_loss=0.6921 kd_loss=0.0315
Epoch [01/03] Step [002/025]: acc=0.5000 g_loss=0.6933 d_loss=0.6917 kd_loss=0.0324
Epoch [01/03] Step [003/025]: acc=0.5000 g_loss=0.6878 d_loss=0.6903 kd_loss=0.1795
Epoch [01/03] Step [004/025]: acc=0.5000 g_loss=0.6833 d_loss=0.6909 kd_loss=0.2962
Epoch [01/03] Step [005/025]: acc=0.5000 g_loss=0.6819 d_loss=0.6875 kd_loss=0.0838
Epoch [01/03] Step [006/025]: acc=0.5000 g_loss=0.6774 d_loss=0.6887 kd_loss=0.1287
Epoch [01/03] Step [007/025]: acc=0.5000 g_loss=0.6669 d_loss=0.6900 kd_loss=0.2110
Epoch [01/03] Step [008/025]: acc=0.5000 g_loss=0.6679 d_loss=0.6901 kd_loss=0.3633
Epoch [01/03] Step [009/025]: acc=0.5000 g_loss=0.6651 d_loss=0.6907 kd_loss=0.1907
Epoch [01/03] Step [010/025]: acc=0.5000 g_loss=0.6683 d_loss=0.6866 kd_loss=0.1102
Epoch [01/03] Step [011/025]: acc=0.5000 g_loss=0.6687 d_loss=0.6887 kd_loss=0.1025
Epoch [01/03] Step [012/025]: acc=0.5000 g_loss=0.6659 d_loss=0.6833 kd_loss=0.0687
Epoch [01/03] Step [013/025]: acc=0.5000 g_loss=0.6542 d_loss=0.6896 kd_loss=0.1012
Epoch [01/03] Step [014/025]: acc=0.5000 g_loss=0.6460 d_loss=0.6934 kd_loss=0.2312
Epoch [01/03] Step [015/025]: acc=0.5000 g_loss=0.6478 d_loss=0.6919 kd_loss=0.1715
Epoch [01/03] Step [016/025]: acc=0.5000 g_loss=0.6605 d_loss=0.6808 kd_loss=0.0783
Epoch [01/03] Step [017/025]: acc=0.5000 g_loss=0.6661 d_loss=0.6801 kd_loss=0.0870
Epoch [01/03] Step [018/025]: acc=0.5000 g_loss=0.6553 d_loss=0.6858 kd_loss=0.0376
Epoch [01/03] Step [019/025]: acc=0.5000 g_loss=0.6704 d_loss=0.6712 kd_loss=0.0330
Epoch [01/03] Step [020/025]: acc=0.5000 g_loss=0.6665 d_loss=0.6859 kd_loss=0.1410
Epoch [01/03] Step [021/025]: acc=0.5000 g_loss=0.6707 d_loss=0.6756 kd_loss=0.0994
Epoch [01/03] Step [022/025]: acc=0.5000 g_loss=0.6291 d_loss=0.6911 kd_loss=0.0608
Epoch [01/03] Step [023/025]: acc=0.5000 g_loss=0.6583 d_loss=0.6795 kd_loss=0.0596
Epoch [01/03] Step [024/025]: acc=0.5000 g_loss=0.6414 d_loss=0.6871 kd_loss=0.0698
Epoch [01/03] Step [025/025]: acc=0.5000 g_loss=0.6357 d_loss=0.6834 kd_loss=0.1144
Avg Loss = 1.2234, Avg Accuracy = 0.5640
Epoch [02/03] Step [001/025]: acc=0.5000 g_loss=0.6149 d_loss=0.6890 kd_loss=0.0727
Epoch [02/03] Step [002/025]: acc=0.5000 g_loss=0.6177 d_loss=0.6846 kd_loss=0.1580
Epoch [02/03] Step [003/025]: acc=0.5000 g_loss=0.6213 d_loss=0.6809 kd_loss=0.1119
Epoch [02/03] Step [004/025]: acc=0.5000 g_loss=0.6188 d_loss=0.6873 kd_loss=0.1278
Epoch [02/03] Step [005/025]: acc=0.5000 g_loss=0.6154 d_loss=0.6856 kd_loss=0.1290
Epoch [02/03] Step [006/025]: acc=0.5000 g_loss=0.6321 d_loss=0.6838 kd_loss=0.1556
Epoch [02/03] Step [007/025]: acc=0.5000 g_loss=0.6374 d_loss=0.6798 kd_loss=0.0656
Epoch [02/03] Step [008/025]: acc=0.5000 g_loss=0.6340 d_loss=0.6799 kd_loss=0.0272
Epoch [02/03] Step [009/025]: acc=0.5000 g_loss=0.6204 d_loss=0.6860 kd_loss=0.0697
Epoch [02/03] Step [010/025]: acc=0.5000 g_loss=0.6072 d_loss=0.6986 kd_loss=0.0819
Epoch [02/03] Step [011/025]: acc=0.5000 g_loss=0.6156 d_loss=0.6790 kd_loss=0.0411
Epoch [02/03] Step [012/025]: acc=0.5000 g_loss=0.6009 d_loss=0.7023 kd_loss=0.0549
Epoch [02/03] Step [013/025]: acc=0.5000 g_loss=0.6110 d_loss=0.7004 kd_loss=0.0869
Epoch [02/03] Step [014/025]: acc=0.5000 g_loss=0.5930 d_loss=0.7106 kd_loss=0.0566
Epoch [02/03] Step [015/025]: acc=0.5000 g_loss=0.6388 d_loss=0.6819 kd_loss=0.0182
Epoch [02/03] Step [016/025]: acc=0.5000 g_loss=0.6084 d_loss=0.7070 kd_loss=0.0491
Epoch [02/03] Step [017/025]: acc=0.5000 g_loss=0.6302 d_loss=0.6910 kd_loss=0.0186
Epoch [02/03] Step [018/025]: acc=0.5000 g_loss=0.6340 d_loss=0.7001 kd_loss=0.0490
Epoch [02/03] Step [019/025]: acc=0.5000 g_loss=0.6464 d_loss=0.6892 kd_loss=0.0582
Epoch [02/03] Step [020/025]: acc=0.5000 g_loss=0.6463 d_loss=0.6941 kd_loss=0.0309
Epoch [02/03] Step [021/025]: acc=0.5000 g_loss=0.6703 d_loss=0.6787 kd_loss=0.0500
Epoch [02/03] Step [022/025]: acc=0.5000 g_loss=0.6679 d_loss=0.6885 kd_loss=0.0560
Epoch [02/03] Step [023/025]: acc=0.5000 g_loss=0.6729 d_loss=0.6871 kd_loss=0.0888
Epoch [02/03] Step [024/025]: acc=0.5000 g_loss=0.6645 d_loss=0.6932 kd_loss=0.0758
Epoch [02/03] Step [025/025]: acc=0.5000 g_loss=0.6762 d_loss=0.6894 kd_loss=0.0844
Avg Loss = 1.2287, Avg Accuracy = 0.5650
Epoch [03/03] Step [001/025]: acc=0.5000 g_loss=0.6791 d_loss=0.7010 kd_loss=0.0751
Epoch [03/03] Step [002/025]: acc=0.5000 g_loss=0.6854 d_loss=0.6852 kd_loss=0.0591
Epoch [03/03] Step [003/025]: acc=0.5000 g_loss=0.6769 d_loss=0.6988 kd_loss=0.0482
Epoch [03/03] Step [004/025]: acc=0.5000 g_loss=0.6891 d_loss=0.6918 kd_loss=0.0997
Epoch [03/03] Step [005/025]: acc=0.5000 g_loss=0.7052 d_loss=0.6795 kd_loss=0.0519
Epoch [03/03] Step [006/025]: acc=0.5000 g_loss=0.7032 d_loss=0.6893 kd_loss=0.0421
Epoch [03/03] Step [007/025]: acc=0.5000 g_loss=0.6897 d_loss=0.6919 kd_loss=0.0223
Epoch [03/03] Step [008/025]: acc=0.5000 g_loss=0.6960 d_loss=0.6889 kd_loss=0.0317
Epoch [03/03] Step [009/025]: acc=0.5000 g_loss=0.6967 d_loss=0.7048 kd_loss=0.0716
Epoch [03/03] Step [010/025]: acc=0.5000 g_loss=0.6790 d_loss=0.7010 kd_loss=0.0290
Epoch [03/03] Step [011/025]: acc=0.5000 g_loss=0.6750 d_loss=0.6998 kd_loss=0.1050
Epoch [03/03] Step [012/025]: acc=0.5000 g_loss=0.6857 d_loss=0.6874 kd_loss=0.0267
Epoch [03/03] Step [013/025]: acc=0.5000 g_loss=0.6858 d_loss=0.6936 kd_loss=0.1236
Epoch [03/03] Step [014/025]: acc=0.5000 g_loss=0.6809 d_loss=0.6912 kd_loss=0.0447
Epoch [03/03] Step [015/025]: acc=0.5000 g_loss=0.6746 d_loss=0.7061 kd_loss=0.0416
Epoch [03/03] Step [016/025]: acc=0.5000 g_loss=0.6748 d_loss=0.7020 kd_loss=0.0799
Epoch [03/03] Step [017/025]: acc=0.5000 g_loss=0.6967 d_loss=0.6789 kd_loss=0.0430
Epoch [03/03] Step [018/025]: acc=0.5000 g_loss=0.6850 d_loss=0.6892 kd_loss=0.0708
Epoch [03/03] Step [019/025]: acc=0.5000 g_loss=0.6961 d_loss=0.6813 kd_loss=0.0826
Epoch [03/03] Step [020/025]: acc=0.5000 g_loss=0.6783 d_loss=0.6950 kd_loss=0.0685
Epoch [03/03] Step [021/025]: acc=0.5000 g_loss=0.6788 d_loss=0.6987 kd_loss=0.0482
Epoch [03/03] Step [022/025]: acc=0.5000 g_loss=0.6842 d_loss=0.6868 kd_loss=0.1489
Epoch [03/03] Step [023/025]: acc=0.5000 g_loss=0.6901 d_loss=0.6809 kd_loss=0.0351
Epoch [03/03] Step [024/025]: acc=0.5000 g_loss=0.6749 d_loss=0.6964 kd_loss=0.0639
Epoch [03/03] Step [025/025]: acc=0.5000 g_loss=0.6792 d_loss=0.6989 kd_loss=0.0434
Avg Loss = 1.1886, Avg Accuracy = 0.5900
=== Evaluating classifier for encoded target domain ===
>>> source only <<<
Avg Loss = 1.0161, Avg Accuracy = 0.5820
>>> domain adaption <<<
Avg Loss = 1.1578, Avg Accuracy = 0.5900
