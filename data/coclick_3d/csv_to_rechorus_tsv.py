from cgi import test
import pandas as pd 
import numpy as np

print("HELLO")


TRAIN_CSV= '/home/azureuser/cloudfiles/data/dataset/train_csv_3d/Output2'
TEST_CSV = '/home/azureuser/cloudfiles/data/dataset/test_3d_csv/Tsv'
VALIDATION_CSV= '/home/azureuser/cloudfiles/data/dataset/validation_3d_csv/Tsv'


#Convert CSV to TSV

train_df= pd.read_csv(TRAIN_CSV, sep=',', index_col=False)
train_df.columns= ['user_id', 'item_id', 'edge_weight']
train_df= train_df[['user_id', 'item_id']]

test_df= pd.read_csv(TEST_CSV, sep=',')
test_df.columns= ['user_id', 'item_id']

validation_df= pd.read_csv(VALIDATION_CSV, sep=',' )
validation_df.columns= ['user_id', 'item_id']





def id_indexing_from_one(df):
    df['user_id']= df['user_id']+1
    df['item_id']= df['item_id']+1
    return df

   
train_df= id_indexing_from_one(train_df)
test_df= id_indexing_from_one(test_df)
validation_df= id_indexing_from_one(validation_df)


def add_time_column(df):
    df['time']= np.arange(df.shape[0])
    return df

train_df= add_time_column(train_df)
test_df= add_time_column(test_df)
validation_df= add_time_column(validation_df)

NUM_NEGS= 10
def add_negative_items(df, num_negs):
    num_items = df.item_id.nunique()
    print(f"Number of items: {num_items}")
    num_rows= df.shape[0]
    df['neg_items']= np.random.randint(1, num_items+1, (num_rows,NUM_NEGS)).tolist()

    #df['neg_items']= df['neg_items'].apply(lambda x: x.to_list())
    return df

test_df= add_negative_items(test_df, NUM_NEGS)
validation_df= add_negative_items(validation_df, NUM_NEGS)




RECHORUS_TRAIN_TSV= "train.csv"
RECHORUS_TEST_TSV= "test.csv"
RECHORUS_VALIDATION_TSV= "dev.csv"

train_df.to_csv(RECHORUS_TRAIN_TSV, sep='\t', index=False)
test_df.to_csv(RECHORUS_TEST_TSV, sep='\t', index=False)
validation_df.to_csv(RECHORUS_VALIDATION_TSV, sep='\t', index=False)


