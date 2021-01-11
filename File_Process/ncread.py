import netCDF4 as nc
file = r'C:\Users\Apple\Desktop\clt_day_FGOALS-g2_historical_r1i1p1_19690101-19691231.nc'
dataset = nc.Dataset(file)
print(dataset.variables.keys())
print(dataset.variables["lat_bnds"][:])
