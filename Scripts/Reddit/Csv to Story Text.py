# Script to change csv to text to get stories.

import pandas as pd
from tqdm import tqdm


csv_file_name = ""

nosleep_dataset_Raw_Csv_1_Filterd = pd.read_csv(csv_file_name)


for i in tqdm(range(int((nosleep_dataset_Raw_Csv_1_Filterd.shape[0])/4))):
    open(csv_file_name, 'a', encoding="utf-8").write(str(nosleep_dataset_Raw_Csv_1_Filterd.iloc[[i][0]].body))


for i in tqdm(range(100)):
    open(csv_file_name+'_Text.txt', 'a', encoding="utf-8").write(str(nosleep_dataset_Raw_Csv_1_Filterd.iloc[[i][0]].body))
