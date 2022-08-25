import pandas as pd
from sklearn.model_selection import StratifiedKFold

import json
train = pd.read_json("../input/tig-stainless-steel-304/ss304/train/train.json", orient='index')
train['path'] = "../input/tig-stainless-steel-304/"+train.index
train.reset_index(drop=True, inplace=True)
train.rename(columns = {0:'Label'}, inplace = True)
train.head()

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
oof = []
targets = []
target = "Label"

for fold, (trn_idx, val_idx) in enumerate(
    skf.split(train, train[target])
):
    train.loc[val_idx, "fold"] = int(fold)


train.to_csv("../train.csv", index=False)