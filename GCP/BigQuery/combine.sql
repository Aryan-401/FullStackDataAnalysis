create or replace table `new-york-cab-data-analysis.nyc_taxi_data.flat_file_data_analysis` AS (

select f.VendorID, d.tpep_pickup_datetime, d.tpep_dropoff_datetime, p.PULocation_x, p.PULocation_y, dr.DOLocation_x, dr.DOLocation_y, pa.passenger_count, pay.payment_type_name, r.rate_code_name, t.trip_distance, f.fare_amount, f.extra, f.mta_tax, f.tip_amount, f.tolls_amount, f.improvement_surcharge
 from `new-york-cab-data-analysis.nyc_taxi_data.fact_table` f
join `new-york-cab-data-analysis.nyc_taxi_data.datetime_dim` d on d.datetime_id = f.datetime_id
join `new-york-cab-data-analysis.nyc_taxi_data.PU_location_dim` p on p.PU_location_id = f.PU_location_id
join `new-york-cab-data-analysis.nyc_taxi_data.DO_location_dim` dr on dr.DO_location_id = f.DO_location_id
join `new-york-cab-data-analysis.nyc_taxi_data.passenger_count_dim` pa on pa.passenger_count_id = f.passenger_count_id
join `new-york-cab-data-analysis.nyc_taxi_data.payment_type_dim` pay on pay.payment_type_id = f.payment_type_id
join `new-york-cab-data-analysis.nyc_taxi_data.rate_code_dim` r on r.rate_code_id = f.rate_code_id
join `new-york-cab-data-analysis.nyc_taxi_data.trip_distance_dim` t on t.trip_distance_id = f.trip_distance_id
)
