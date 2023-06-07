import pandas as pd
df_ = pd.DataFrame({})
for i in range(1, 13):

    if i < 10:
        month = '0'+str(i)
    else:
        month = str(i)

    df = pd.read_parquet(f'yellow_tripdata_2022-{month}.parquet')
    df_ = pd.concat([df_, df])
    print(f'{df_.shape}, {i}/12')

df_.to_csv('yellow_tripdata_2022.csv', index=False)



