# **dehaze**
The implementation of a haze removal algorithm according to the color attenuation prior.

Based on the [paper](https://ieeexplore.ieee.org/document/7128396) by Qingsong Zhu, Jiaming Mai, and Ling Shao, published in the IEEE Transactions on Image Processing, Volume 24 Issue 11.

## Running the Code
To run the code, run the following command from the ``/dehaze/source`` directory:

 ``python test.py``
    
This will run the dehazing on all six test images given in the ``/dehaze/images`` directory. The dehazed images will be saved in their respective folders, along with their corresponding raw and final depth maps.

To run the algorithm on your own image, manually add a test case to the test.py file in the given format.

## Results
Dehazing works well but this implementation adds halo artifacts and haze to foreground for some reason.

### City
Original (1); Dehazed (2); Raw Depth Map (3); Final Depth Map (4)

![city comparison](/images/tests/city/city_comp.png "City") 

### Canyon
Original (1); Dehazed (2); Raw Depth Map (3); Final Depth Map (4)

![canyon comparison](/images/tests/canyon/canyon_comp.png "Canyon") 

### France
Original (1); Dehazed (2); Raw Depth Map (3); Final Depth Map (4)

![france comparison](/images/tests/france/france_comp.png "France") 

### Swiss
Original (1); Dehazed (2); Raw Depth Map (3); Final Depth Map (4)

![swiss comparison](/images/tests/swiss/swiss_comp.png "Swiss") 

### Plane
Original (1); Dehazed (2); Raw Depth Map (3); Final Depth Map (4)

![plane comparison](/images/tests/plane/plane_comp.png "Plane") 

### Canyon 2
Original (1); Dehazed (2); Raw Depth Map (3); Final Depth Map (4)

![canyon 2 comparison](/images/tests/canyon2/canyon2_comp.png "Canyon 2") 
