import pandas as pd

anno_dir_1="../../../data/guangdong1_round1_train1_20190818/Annotations/anno_train.json"
anno_dir_2="../../../data/guangdong1_round1_train2_20190828/Annotations/anno_train.json"

anno_result_1= pd.read_json(open(anno_dir_1,"r"))
anno_result_2= pd.read_json(open(anno_dir_2,"r"))

frames =[anno_result_1, anno_result_2]
anno_result = pd.concat(frames)
print("done")