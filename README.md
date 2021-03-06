# Health4You
This is my submission for a Timathon competition. The project's name is Health4You and it includes 6 subprojects in it. This is an allround project that works on staying fit, intaking enough calories, checking your energy index, etc. This app was made using PyQt5. Demonstration of the project - https://www.youtube.com/watch?v=xi7vMahyofc
**Please note there are problems with the main.exe file after you extract the downloaded zipped folder. 2 Possible fixes are given below**. 

## How do you setup the project

## Method 1 to setup the project (using the MAIN.py file)
First as always, you have to download the repository by clicking on the green code button on the top right and clicking "Download Zip", once this is done make sure to extract it. After you are done extracting it, open CMD in the same directory of the MAIN.py file, then say 
```pip install -r requirements.txt```, 
for this you will have to have pip and python installed. After running this command, you should have all the required modules like PyQt5, requests, tensorflow, etc. Finally make sure to run the MAIN.py file. Now you are good to go! If you don't have python installed, please view method 2. 

### Video link on how to setup the project using the MAIN.py file - https://www.youtube.com/watch?v=8VZvJhovP7o

## Method 2 to setup the project (using the exe file)
To setup the project, the first thing that you have to do is download the zip of the repository by clicking on the green code button on the top right and clicking "Download Zip", once this is done make sure to extract it. Once this is done go into the subfolder "Health4You" and you will see all the files and folders of the project. Ideally you would want to run the exe file, but github is causing a few problems with the exe. So now I will give two fixes for the said problem. **Please note that windows defender may say that there is a virus in the exe, don't be afraid this is a false positive, there are no such issues with the file.** Video links for both the fixes have been attached - 

### Fix 1 video link -  https://www.youtube.com/watch?v=yyBfWIV8Cz0
### Fix 2 video link -  https://www.youtube.com/watch?v=XMwYacoqPuk
If your problem hasnt been fixed then these two videos will surely be able to help you out.

### **Fix 1**
After downloading the files and then extracting, you should download the main.exe file seperately by clicking on that file and downloading it. If you do this step then it is important to put the exe file in the same directory as the MAIN.py file. The exe file that you have now downloaded should have a file size of about 6,00,000 KB. Whereas the previous exe file that you saw wouldve been only 1KB. Make sure to replace the 1KB exe file with the exe file that you have downloaded seperately

### **Fix 2**
This is the second fix and the fix that I suggest you go for. I have attached a google drive link - https://drive.google.com/drive/folders/1o9uAPCUKdd_-pmw21dhSC-zy1aqLihtc?usp=sharing
You can use this link to download all the files directly from there, in this case there won't be any problems with the exe file. But one thing you have to note is that you may get warning saying that the exe file has a virus in it, fret not I have tried this on multiple machines and there are no issues with the exe file. Even in this fix, you have to download the exe file seperately, put it in the same directory as the MAIN.py file and then run it. But I do understand your concern so I have also given another method (method 1) to setup the project without the use of the exe file.

## Info on the subprojects
The 6 projects that are a part of this app are

### **1. FitZone**

This is a project that takes in your gender, age, your daily physical activity, whether you have health issues, your weight and your height and then generates the number of       calories you burn per day on average, your bmi, the calories that you have to intake per day and also the perfect weight for your height using various formulae. The most           important part of this app is, if you are overweight this app generates a list of various exercises to lose the required weight in a stipulated time. It works on keeping the       user fit and healthy and I guarentee that if you follow these drills you are bound to lose weight.

### **2. CovidScan**

This is an AI model, that uses CNN(Convolutional Neural Networks) to understand whether the chest CT scan of a patient is a covid patients CT scan or a normal persons CT scan.
This AI model has been trained on 6000 different images and has an accuracy of 96%. Once you setup the project(*Info on that has been given above*) you will see sample CT scans of covid patients on your right hand side. Please only upload such types of images in the upload image section. This subproject outputs its prediction, the model remarks and its confidence.

### **3. Dietning**

This project, takes in various inputs like gender, age, physical activity, whether you have health issues and the number of meals you want to eat per day and generates a tasty but healthy diet to reach perfect weight. The various inputs are used to understand your required calorie intake and the diet is generated based on that.The projects name is short hand for "Diet Planning" and it shows that if you follow the diet provided by the subproject, you can lose weight and become fit as fast as "lightning". 
~~I know its a bit cringe but thats how it is.~~ . Here are the different meals that are suggested based on the meals you want to eat per day - 

 a) 1 meal - generates one main meal
 b) 2 meals - generates breakfast and lunch
 c) 3 meals - generates breakfast, lunch and dinner
 d) 4 meals - generates breakfast, lunch, snack and dinner
 e) 5 meals - generates breakfast, lunch, snack, dinner and desert
 
### **4. Hospiloc**
This project's name is shorthand for "hospital locations". Based on your address, it gives you a list of 5 different hospitals near you and the hospitals information like their phone number, address, name, etc. The app then generates a map, which has all the five hospitals marked on it. The address that has to be provided has to be in a specific format, which is specified in the project itself.
 
### **5. EnergyIndex**
This project also uses AI to predict how burned out you are on a scale of 0 to 1. It is specific for employees in companies. The various inputs that it takes are - your gender, your designation in the company on a scale of 0 to 5(0 being the lowest designation and 5 being the highest), whether your company allows a work from home setup(WFH setup), the hours that you have to work for per day on a scale of 0 to 10(0 being the lowest and 10 the highest) and also how stressed you feel, it then outputs how burned out you are on a scale of 0 to 1.

### **6. Dietning 2**
This project is a continuasion of the first and third projects. This project takes in the number of calories that you want to eat per day and the number of meals that you want to eat per day and then generates a diet based on that. In some cases, the first project(*FitZone*), says that if you intake a certain number of calories per day(this calorie amount will be what's required for your age and other factors) you will automatically lose weight without doing any extra exercise, this is based on the fact that on average you burn more calories, then the required calories that are generated for you. In those cases, you can visit this project and enter the number of calories that you want to intake and a diet for that amount of calories will be supplied.

## Important shortcut keys
enter - this gives the prediction/output of a specific model or subproject.
Shift + B - this takes you back to the home screen


## Feeback
Please star the github repo, if you liked it. Also kindly send your feedback whether it may be positive or negative to ananthramtennis12@gmail.com. Cheers!

## Images of the project

### This is the image of the main page ie the first three projects


![alt text](https://github.com/PythonIsInMyGenes/Health4You/blob/main/images/Main%20Page.png)



### Below you will find the image of the first project, "FitZone"


![alt text](https://github.com/PythonIsInMyGenes/Health4You/blob/main/images/FitoneImage.png)



### This is the second project, "CovidScan"


![alt text](https://github.com/PythonIsInMyGenes/Health4You/blob/main/images/CovidScanImage.png)



### Next, you will see the third project, "Dietning"


![alt text](https://github.com/PythonIsInMyGenes/Health4You/blob/main/images/Dietning%20image.png)



### Below, you will find the generated map of the fourth project, "HospiLoc"


![alt text](https://github.com/PythonIsInMyGenes/Health4You/blob/main/images/Hospitals_image.png)



### Lastly, you will see the image of the fifth project, "EnergyIndex"


![alt text](https://github.com/PythonIsInMyGenes/Health4You/blob/main/images/EnergyIndex.png)



There is also a sixth project, called "Dietning 2" which is a continuasion of the first and third project.
