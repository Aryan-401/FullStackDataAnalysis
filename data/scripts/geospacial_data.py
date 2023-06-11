import geopandas as gpd

data = gpd.read_file('../NYC Taxi Zones.geojson')
data['centroid'] = data['geometry'].centroid

data['coordinate_x'] = data['centroid'].apply(lambda p: p.x)
data['coordinate_y'] = data['centroid'].apply(lambda p: p.y)

data[['location_id', 'zone', 'coordinate_x', 'coordinate_y']].to_csv('../taxi_zones.csv', index=False)

