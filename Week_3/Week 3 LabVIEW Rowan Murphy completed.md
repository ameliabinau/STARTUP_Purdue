# Week 3 Homework - LabVIEW Practice 

**LabVIEW is a software that allows for control, measurement, and manipulation of signals/data from hardware in a lab.** It can also be used to program mathematical calculations and other logical flows. LabVIEW programs can be found in just about every experimental physics lab as it serves as an easy "integrator" for instrument measurements.

LabVIEW (created by National Instruments, NI) uses a "visual" programming language called G and is coded in various C languages (https://en.wikipedia.org/wiki/LabVIEW). There is a "front end" (or "**front panel**") to the software, where displays of information (plots, "lights" signifying binary signals, switches, buttons, numeric displays, etc.) can be created that show the status of data as it's being manipulated in the "back end" or "**block diagram**" of the program. 

**Download LabVIEW** (https://www.ni.com/en/support/downloads/software-products/download.labview-student-software-suite.html#352828) from NI. You automatically get a 45 day trial of the software. You'll have to create a NI account using your Purdue email. Once this is done and you verify your account via email, you begin the download of the LabVIEW suite. If you run Windows, they will ask if you want to disable Windows Fast Startup; click no. Additionally, you don't want to install any of the additional packages for LabVIEW; the program might take around 10 minutes to install anyway and we won't need them, we'll just need the base software. After it installs, your computer will restart. Launch LabVIEW when complete and click "Create Project" and "Create New VI." Every project will be called a "VI," or "Virtual Instrument." 

***Please review this introductory summary** of the two different panels that are generated when you create a new project: https://learn.ni.com/learn/article/labview-tutorial*

### **Activity 1:**

Explore the "Functions" window. Name three functions from three major categories (drop-down boxes) and describe what they are used for. You can do a little research for this. 

1. In Programming -> Structures, there is a for loop. A for loop is usually used to iterate through multiple things, like if you wanted to go through each piece of data in a dataset (although this is not always the most efficient way to do this).
There is also an event structure. Usually this is used when you only want something to happen if some requirement (case) is met.
Lastly theres a case structure, which is at first I got confused with the event structure. This on the other hand has cases inside it, and when one of them executes, the rest of them inside do as well.

2. In data communication there are local and global variables. Local variables are only useable in that VI, meaning the one you have open and create it in. On the other hand, global variables are useable in ALL VIs you have, not just the one you created it in. This would be good for creating constants like big G, speed of light, etc.

3. In Signal Processing -> Waveform Generation there is Basic Function Generation. It does basically what it sounds like, it takes in a bunch of parameters and creates a waveform based on your inputs and signal type.



### **Activity 2: Wein's Law Calculator**

**BTW** - If at any point you exit your VI, reopen it, and either the Block Diagram or Front Panel are missing, just go to Window -> Show Block Diagram/Show Front Panel to reopen it. I've found LabVIEW tends to open with just the Front Panel, which makes sense - when you've completed creating a working LabVIEW program and are using it for science/data collection, you'll use the Front Panel (this is the interactive and data-readout part) much more than the Block Diagram. 

**Wein's Law** is an intrinsic law of bulk materials describing the peak wavelength (m) of an object's emitted **electromagnetic blackbody spectrum** at a given temperature (K). Read more here: https://en.wikipedia.org/wiki/Wien%27s_displacement_law. Let's create a simple LabVIEW program that takes a numeric input (in Kelvin) and outputs the corresponding, theoretical peak wavelength in nanometers (nm). Normally, LabVIEW is used to take such input values from an instrument in the lab and run calculations, but it can also be used to create simple calculators like this, too. The equation for Wein's Law is: $\lambda_{peak} = m/T$, where m is a constant equal to about 0.002897 m*K. 

**1.** In your new VI, navigate to the Front Panel and find the "Controls" window. It should automatically appear when you open the VI. If it does not, go to View -> Control Palette at the top of the Front Panel. Then, in the Controls window, click on Modern -> Numeric. Under this tab, create a single Numeric Control AND a single Numeric Indicator in the Front Panel interface. Rename the Numeric Control "Temperature (K)" and the Numeric Indicator "Wavelength (nm)." The Numeric Control allows us to input some value for the temperature of our object, in Kelvin, and the Numeric Indicator will produce the result of our Wein's Law calculation once the LabVIEW program is run.

**2.** Navigate to the Block Diagram panel. If it is not already open, navigate to View -> Function Palette and open the Functions Window. Notice that two blocks were automatically generated when we created the Numeric Control and Indicator in the Block View -> these respresent where our input and output come in and out of our "circuit." In the Functions window, navigate to Mathematics -> Numeric and place a "Multiplication" and a "Division" operator somewhere in the block diagram.

**3.** Let's add the multiplicative m constant and a $10^9$ multiplier to make the output result be expressed in nanometers (reminder, the m constant will produce a value in units of m*K, so we must multiply that value by $10^9$ to put it in nm). In Mathematics -> Numeric, place two DBL Numeric Constants into the block diagram. Input "0.002897" into one block and "1000000000" into the other block. 

**4.** Alright, we should have six "blocks" in our block diagram. It's time to connect them, maintaining order of operations, such that the input data (Temperature) from our Front Panel is manipulated according to the Wein's Law equation and the output is the peak wavelength in nm. Order the blocks, from left to right, according to order of opperations. By clicking on the circles that appear on the edges of each block, you can connect them using numeric "wires." To use the mupliplication and division blocks, two input wires (the two numbers being multiplied or divided) are attached at the left of the triangle, the top wire being the first number (numerator) and the bottom being the second (denominator). Then, the "point" of the triangle is where the output wire starts. Using this information, create the complete circuit. Use video or pictoral resources (see the Tutorial above Activity 1) if needed.

**5.** Once the dataflow "circuit" is setup, it's time to run the LabVIEW program. Navigate to the Front Panel and type a temperature of 1000 K into the "Temperature (K)" input. Then, at the top left of the panel, press the right-pointing arrow to run the program. A new number - the output - should appear in the results box. What number does it yeild? If done correctly, it should yeild approximately 2897 nm. That is, an object with an average temperature of 1000 K emits thermal radiation with a wavelength of 2897 nm, which is in the infrared.

**6.** The temperature of the Sun is approx. 5780 K. Use your LabVIEW calculator to determine what wavelength the Sun emits most of. What color does this wavelength correspond to? In a `.md` file in GitHub, answer this question and insert screenshots of your Block Diagram and Front Panel for this LabVIEW program. Congrats! You just created your first fully-functional LabVIEW program. Imagine how you could use this program to collect data taken from hardware in a lab and record/manipulate it using our "circuits" in real-time!

1. From a temperature of 5780 K, it emits around 501 nm, which is between green and blue light on the spectrum (closer to green), but we do not see the sun as green. I actually just looked up why and it has to do with a lot of things.

![alt text](image.png)

I don't think this image actually works, so I'm just going to upload mine to GitHub with this .md file.


