import pgm
import util
import dehaze

# Test One: City

print("~~~~~~~~~~~~~~")
print("Test One: City")
print("~~~~~~~~~~~~~~")

print("Reading image...")

city = pgm.readppm("../images/tests/city/city.ppm")

print("Calculating raw depth map...")

city_raw = dehaze.raw_depth_map(city)

print("Saving raw depth map...")

pgm.writepgm("../images/tests/city/city_rdm.pgm", city_raw)

print("Restoring depth map...")

cityfdm = dehaze.final_depth_map(city_raw)

print("Saving depth map...")

scaled_fdm = util.scale_data(cityfdm, 255)

pgm.writepgm("../images/tests/city/city_fdm.pgm", scaled_fdm)

print("Restoring...")

restore_city = dehaze.restore_img(city, cityfdm) 

print("Saving restored image...")

pgm.writeppm("../images/tests/city/restore_city.ppm", restore_city)

# Test Two: Canyon

print("~~~~~~~~~~~~~~~~~")
print("Test Two: Canyon")
print("~~~~~~~~~~~~~~~~~")

print("Reading image...")

canyon = pgm.readppm("../images/tests/canyon/canyon.ppm")

print("Calculating raw depth map...")

canyon_raw = dehaze.raw_depth_map(canyon)

print("Saving raw depth map...")

pgm.writepgm("../images/tests/canyon/canyon_rdm.pgm", canyon_raw)

print("Restoring depth map...")

canyonfdm = dehaze.final_depth_map(canyon_raw)

print("Saving depth map...")

scaled_fdm = util.scale_data(canyonfdm, 255)

pgm.writepgm("../images/tests/canyon/canyon_fdm.pgm", scaled_fdm)

print("Restoring...")

restore_canyon = dehaze.restore_img(canyon,canyonfdm) 

print("Saving restored image...")

pgm.writeppm("../images/tests/canyon/restore_canyon.ppm", restore_canyon)

# Test Three: France

print("~~~~~~~~~~~~~~~~~~")
print("Test Three: France")
print("~~~~~~~~~~~~~~~~~~")

print("Reading image...")

france = pgm.readppm("../images/tests/france/france.ppm")

print("Calculating raw depth map...")

france_raw = dehaze.raw_depth_map(france)

print("Saving raw depth map...")

pgm.writepgm("../images/tests/france/france_rdm.pgm", france_raw)

print("Restoring depth map...")

francefdm = dehaze.final_depth_map(france_raw)

print("Saving depth map...")

scaled_fdm = util.scale_data(francefdm, 255)

pgm.writepgm("../images/tests/france/france_fdm.pgm", scaled_fdm)

print("Restoring...")

restore_france = dehaze.restore_img(france, francefdm) 

print("Saving restored image...")

pgm.writeppm("../images/tests/france/restore_france.ppm", restore_france)

# Test Four: Swiss

print("~~~~~~~~~~~~~~~~")
print("Test Four: Swiss")
print("~~~~~~~~~~~~~~~~")

print("Reading image...")

swiss = pgm.readppm("../images/tests/swiss/swiss.ppm")

print("Calculating raw depth map...")

swiss_raw = dehaze.raw_depth_map(swiss)

print("Saving raw depth map...")

pgm.writepgm("../images/tests/swiss/swiss_rdm.pgm", swiss_raw)

print("Restoring depth map...")

swissfdm = dehaze.final_depth_map(swiss_raw)

print("Saving depth map...")

scaled_fdm = util.scale_data(swissfdm, 255)

pgm.writepgm("../images/tests/swiss/swiss_fdm.pgm", scaled_fdm)

print("Restoring...")

restore_swiss = dehaze.restore_img(swiss, swissfdm) 

print("Saving restored image...")

pgm.writeppm("../images/tests/swiss/restore_swiss.ppm", restore_swiss)

# Test Five: Plane

print("~~~~~~~~~~~~~~~~")
print("Test Five: Plane")
print("~~~~~~~~~~~~~~~~")

print("Reading image...")

plane = pgm.readppm("../images/tests/plane/plane.ppm")

print("Calculating raw depth map...")

plane_raw = dehaze.raw_depth_map(plane)

print("Saving raw depth map...")

pgm.writepgm("../images/tests/plane/plane_rdm.pgm", plane_raw)

print("Restoring depth map...")

planefdm = dehaze.final_depth_map(plane_raw)

print("Saving depth map...")

scaled_fdm = util.scale_data(planefdm, 255)

pgm.writepgm("../images/tests/plane/plane_fdm.pgm", scaled_fdm)

print("Restoring...")

restore_plane = dehaze.restore_img(plane, planefdm) 

print("Saving restored image...")

pgm.writeppm("../images/tests/plane/restore_plane.ppm", restore_plane)

# Test Six: Canyon 2

print("~~~~~~~~~~~~~~~~~~~~")
print("Test Six: Canyon 2")
print("~~~~~~~~~~~~~~~~~~~~")

print("Reading image...")

canyon2 = pgm.readppm("../images/tests/canyon2/canyon2.ppm")

print("Calculating raw depth map...")

canyon2_raw = dehaze.raw_depth_map(canyon2)

print("Saving raw depth map...")

pgm.writepgm("../images/tests/canyon2/canyon2_rdm.pgm", canyon2_raw)

print("Restoring depth map...")

canyon2fdm = dehaze.final_depth_map(canyon2_raw)

print("Saving depth map...")

scaled_fdm = util.scale_data(canyon2fdm, 255)

pgm.writepgm("../images/tests/canyon2/canyon2_fdm.pgm", scaled_fdm)

print("Restoring...")

restore_canyon2 = dehaze.restore_img(canyon2, canyon2fdm) 

print("Saving restored image...")

pgm.writeppm("../images/tests/canyon2/restore_canyon2.ppm", restore_canyon2)