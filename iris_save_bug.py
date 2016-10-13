import iris

# Load
file1 = 'input.grib2'
cube1 = iris.load(file1)[0]

# Get time
unit1 = cube1.coord('time').units
time1 = unit1.num2date(cube1.coord('time').points)
print time1

# Save
file2 = 'output.grib2'
iris.save(cube1, file2)

# Reload
cube2 = iris.load(file2)[0]

# Get time
unit2 = cube2.coord('time').units
time2 = unit2.num2date(cube2.coord('time').points)
print time2

assert time1[0] == time2[0]
