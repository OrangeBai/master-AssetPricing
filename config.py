import os
from core.utils import *
from sys import platform
all_period = ('1990-01', '2021-01')
period = ('1997-01', '2019-07')

if platform == 'darwin':
    base_directory = r'/Users/oranbebai/Documents/Data/Finance'
else:
    base_directory = r'F:\DataSet\Finance'

raw_directory = os.path.join(base_directory, 'Raw')
csv_directory = os.path.join(base_directory, 'CSV')
feature_directory = os.path.join(base_directory, 'Features')
extracted_directory = os.path.join(base_directory, 'Extracted')
factor_path = os.path.join(base_directory, 'Factors')
output_directory = os.path.join(base_directory, 'Output')
panel_data_directory = os.path.join(base_directory, 'Panel')
panel_data_directory2 = os.path.join(base_directory, 'Panel2')
panel_data_directory3 = os.path.join(base_directory, 'Panel3')
temp_data_path = os.path.join(base_directory, 'Temp_data')
table_directory = os.path.join(base_directory, 'Table')

calendar_path = os.path.join(raw_directory, r'TRD_Cale.txt')
trade_dates = get_trade_dates(calendar_path, period)
all_trade_dates = get_trade_dates(calendar_path, all_period)

month_split_all, quarter_split_all, year_split_all, month_tag_all, quarter_tag_all, year_tag_all = get_split(all_period)
month_split, quarter_split, year_split, month_tag, quarter_tag, year_tag = get_split(period)

co_file = os.path.join(raw_directory, 'TRD_Co.txt')
co_info = pd.read_csv(co_file, sep='\t', encoding='utf8', converters={'Stkcd': str})
co_info = co_info.drop_duplicates(subset='Stkcd', keep='first').set_index('Stkcd')
co_lists = co_info.index.tolist()
co_list_date = co_info['Listdt']

A_info = co_info[(co_info['Markettype'] == 1) | (co_info['Markettype'] == 4) | (co_info['Markettype'] == 16)]
A_lists = A_info.index.tolist()

project_path = get_project_root()

if not os.path.exists(temp_data_path):
    os.makedirs(temp_data_path)
