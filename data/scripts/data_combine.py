import pandas as pd
_df_ = pd.DataFrame()
__df__ = pd.DataFrame()
for i in range(1, 13):

    if i < 10:
        month = '0'+str(i)
    else:
        month = str(i)

    df = pd.read_parquet(f'../yellow_tripdata_2022-{month}.parquet')
    ___df___ = df.sample(n=1600)
    _df_ = pd.concat([_df_, df])
    __df__ = pd.concat([__df__, ___df___])
    print(f'{_df_.shape}, {i}/12')

print('Beginning to save...')
__df__.to_csv('../yellow_tripdata_2022_sample.csv', index=False)
print('Sample saved!')
_df_.to_csv('../yellow_tripdata_2022.csv', index=False)
print('All data saved!')



