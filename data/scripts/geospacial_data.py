import geopandas as gpd
import pandas as pd

data = gpd.read_file('../NYC Taxi Zones.geojson')
data['centroid'] = data['geometry'].centroid

data['coordinate_x'] = data['centroid'].apply(lambda p: p.x)
data['coordinate_y'] = data['centroid'].apply(lambda p: p.y)

data = data[['location_id', 'zone', 'coordinate_x', 'coordinate_y']]
none_values1 = pd.DataFrame({'location_id': 264, 'zone': 'N.A', 'coordinate_x': 0, 'coordinate_y': 0}, index=[263])
none_values2 = pd.DataFrame({'location_id': 265, 'zone': 'N.A', 'coordinate_x': 0, 'coordinate_y': 0}, index=[264])
data = pd.concat([data, none_values1, none_values2])
data.to_csv('../taxi_zones.csv', index=False)

