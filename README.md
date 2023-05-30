# Pixel Project
## Introduction

The software allows you to upload any image you want and create a new, pixelated image of the original image. You can control the size, the number of pixels and the number of shades of the image. Also, it is also possible to get the image pixelated by playing dice, where the shade of the image is determined by the number on the dice.

### Example:

#### Original image:

<img src="Lion.jpg" alt="Image" width="300" height="200">

#### Pixeled image:

<img src="Lion_pixel.jpg" alt="Image" width="300" height="200">

#### Dice pixeled image:

<img src="Lion_dice.jpg" alt="Image" width="300" height="200">

## The program offers the following operations:

1. View the original image.

2. Display the pixelated image.

3. Save a CSV file of the pixelated image with numbers.

4. Draw and save the pixelated image as an ESP file using game cubes.

## Usage
To use the program, follow these steps:

1. Upload the image you want to pixelate to the files folder.

2. Copy the name of the file and paste it in the appropriate place in the code.

3. Run the code and answer the following questions:
    
    a. How many shades would you like for the picture? Note that to draw the pixelated image as game cubes, choose a number less than or equal to 7.
    
    b. How would you like to choose the image size? Based on the total number of pixels or by manually defining the number of rows and columns?
    
    c. How many pixels or how many rows and columns would you like?
    
    d. Would you like to see the original image?
    
    e. Would you like to see the pixelated image?
    
    f. Would you like to save the new image as a CSV file?
    
    g. Would you like to see and save the pixelated image as it is drawn by game cubes?
  
## Prerequisites

Before running the code, ensure that you have the following libraries installed:

pip install math

pip install numpy as np

pip install imageio

pip install matplotlib.pyplot

pip install pandas as pd

pip install turtle

pip install os

Additionally, download the EPS Viewer app [here](https://epsviewer.org/download.aspx) to open the EPS files containing the dice pixel images.
