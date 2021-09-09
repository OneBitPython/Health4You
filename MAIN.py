"""Hello, this is the main file of the project. All classes and files are imported here and main execution takes place here."""


# imports
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import sys
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
import webbrowser
import pyperclip
from hospitals_near_me import FindNearbyHospitals
from diet_planner import GenerateDiet
from concurrent.futures import ThreadPoolExecutor
import requests
import os
import cv2
from tensorflow.keras.models import load_model
import numpy as np
from catboost import CatBoostRegressor
from exercise_planner import ExercisePlanner

# end of imports

# creating main class 'Health'


class Health(QMainWindow):
    def __init__(self):
        super(Health, self).__init__()
        loadUi("design.ui", self)  # loading the design ui
        self.cwd = os.getcwd()
        self.setWindowTitle("Health4You")
        self.InitUi()

    def InitUi(self):
        # creating an empty folder
        if os.path.isdir("covid_images/") == False:
            os.mkdir("covid_images")
        # adding hospital project image for showcasing and also corona project image
        hospital_image_created = QPixmap("images/Hospitals_image.png")
        hospital_image_created = hospital_image_created.scaled(300, 200)
        self.hospital_image.setPixmap(hospital_image_created)

        covid_negative_ct_image = QPixmap("images/Normal patient CT.jpg")
        covid_negative_ct_image = covid_negative_ct_image.scaled(250, 200)
        self.covid_ct_negative_label.setPixmap(covid_negative_ct_image)

        covid_ct_positive = QPixmap("images/Covid patient CT.jpg")
        covid_ct_positive = covid_ct_positive.scaled(250, 200)
        self.covid_ct_positive_label.setPixmap(covid_ct_positive)

        # hide a few buttons and text boxes and set model accuracy values
        self.model_accuracy_bar.setValue(96)
        self.model_burn_accuracy_bar.setValue(93)

        self.hospital_no_1.hide()
        self.hospital_no_2.hide()
        self.hospital_no_3.hide()
        self.hospital_no_4.hide()
        self.hospital_no_5.hide()
        self.open_map_btn.hide()

        self.hospital_no_1.setReadOnly(True)
        self.hospital_no_2.setReadOnly(True)
        self.hospital_no_3.setReadOnly(True)
        self.hospital_no_4.setReadOnly(True)
        self.hospital_no_5.setReadOnly(True)

        self.itemfood_1.hide()
        self.itemfood_2.hide()
        self.itemfood_3.hide()
        self.itemfood_4.hide()
        self.itemfood_5.hide()

        self.itemfood_1.setReadOnly(True)
        self.itemfood_2.setReadOnly(True)
        self.itemfood_3.setReadOnly(True)
        self.itemfood_4.setReadOnly(True)
        self.itemfood_5.setReadOnly(True)

        self.exercises_text_box.setReadOnly(True)
        self.exercises_text_box.hide()

        # hiding buttons and setting read only for 6th project(dietning 2)
        self.itemfood_forcreatediet_1.hide()
        self.itemfood_forcreatediet_1.setReadOnly(True)
        self.itemfood_forcreatediet_2.hide()
        self.itemfood_forcreatediet_2.setReadOnly(True)
        self.itemfood_forcreatediet_3.hide()
        self.itemfood_forcreatediet_3.setReadOnly(True)
        self.itemfood_forcreatediet_4.hide()
        self.itemfood_forcreatediet_4.setReadOnly(True)
        self.itemfood_forcreatediet_5.hide()
        self.itemfood_forcreatediet_5.setReadOnly(True)

        self.predictions_label.hide()

        # setting up ThreadPoolExecutor
        self.thread_executor = ThreadPoolExecutor(max_workers=10)

        # setting limits for burnout project
        self.designation.setRange(0, 5)
        self.resource_allocation.setRange(1, 10)
        self.fatigued_level.setRange(0, 10)

        # setting limits for exercise project
        self.age_exercise_page.setRange(3, 120)
        self.height_exercise_page.setRange(50, 250)
        self.weight_exercise_page.setRange(10, 250)

        # setting imits for 6th project
        self.calories_you_want_to_eat_per_day.setRange(800, 5000)

        # setting up a few default values
        self.gender.setCurrentText("Male")
        self.physical_activity.setCurrentText("1-3 hours")
        self.health_issues.setCurrentText("No")
        self.age.setCurrentText("14-30")
        self.meals_per_day.setCurrentText("3")

        self.gender_exercise_page.setCurrentText("Male")
        self.age_exercise_page.setValue(13)
        self.physical_activity_exercise_page.setCurrentText("1-3 hours")
        self.health_issues_exercise_page.setCurrentText("No")
        self.height_exercise_page.setValue(154)
        self.weight_exercise_page.setValue(60)

        # adding events for button clicks

        # basic btns
        self.developer_info.clicked.connect(self.show_extra_info_for_devs)
        self.next_page_btn.clicked.connect(self.change_to_next_page_func)
        self.prev_page_btn.clicked.connect(self.go_back_to_home)
        self.health_related_info_btn.clicked.connect(
            self.change_page_to_show_health_info
        )
        self.back_to_home_from_health_info.clicked.connect(self.go_back_to_home)

        # buttons for hospiLoc project
        self.back_to_home_from_hospital_page.clicked.connect(self.go_back_to_home)
        self.go_to_hospitals_proj.clicked.connect(self.go_to_hospitals_page)
        self.search_for_hospitals_btn.clicked.connect(self.search_for_hospitals_func)
        self.copy_basic_address_btn.clicked.connect(self.copy_basic_address_func)
        self.open_map_btn.clicked.connect(self.open_map_func)

        # buttons for dietning 1 project
        self.go_to_diet_proj.clicked.connect(self.go_to_diet_page_func)
        self.back_to_home_from_diet_page.clicked.connect(self.go_back_to_home)
        self.generate_meals.clicked.connect(self.generate_meals_func)

        # buttons for covidscan project
        self.go_to_covid_proj.clicked.connect(self.go_to_covid_page_func)
        self.back_to_home_from_covid_page.clicked.connect(self.go_back_to_home)
        self.download_samples_btn.clicked.connect(self.download_samples_thread)
        self.upload_covid_image.clicked.connect(self.upload_image_func)
        self.make_predictions.clicked.connect(self.load_in_image_thread)

        # buttons for energyindex project
        self.go_to_burnout_proj.clicked.connect(self.go_to_burnout_proj_func)
        self.back_to_home_from_burnout_page.clicked.connect(self.go_back_to_home)
        self.predict_whether_burned_out_btn.clicked.connect(
            self.predict_whether_burned_out_func
        )

        # buttons for fitzone project
        self.go_to_exercise_proj.clicked.connect(self.go_to_exercise_proj_func)
        self.back_to_home_from_exercise_page.clicked.connect(self.go_back_to_home)
        self.standard_metric_btn.clicked.connect(self.change_metric_standard)
        self.generate_exercises.clicked.connect(self.generate_exercises_function)

        # buttons for dietning 2 project
        self.go_to_create_diet_proj.clicked.connect(self.go_to_create_diet_proj_func)
        self.back_to_home_from_comeupwithdiet.clicked.connect(self.go_back_to_home)
        self.generate_created_diet.clicked.connect(self.generate_created_diet_func)

        # BTN TO copy github repo
        self.copy_github_repo_link.clicked.connect(self.copy_github_repo_link_func)

    def copy_github_repo_link_func(self):
        """This copies the link to the github repository"""
        pyperclip.copy("https://github.com/PythonIsInMyGenes/Health4You")
        self.copy_label_github_repo.setText("Copied!")

    def set_text_in_boxes_for_diet(
        self,
        item_head,
        txt_for_item_head,
        item_content,
        num,
        all_items,
        calories_of_items,
    ):
        """This function sets texts in the various text boxes and headings for the dietning project"""
        item_head.setText(txt_for_item_head)
        items = ""
        for idx, item in enumerate(all_items[num]):
            items += f"{idx+1}. {item[0]} : {int(item[1])} cal\n"
        items += f"\nTotal Cal : {int(calories_of_items[num])}"
        item_content.setPlainText(items)
        item_content.show()
        item_head.show()

    def generate_created_diet_func(self):
        """This is for the dietning 2 project. It is very similar to the dietning 1 project"""
        calorie_intake_input = self.calories_you_want_to_eat_per_day.value()
        meals_per_day_in_created_diet = self.meals_in_creat_diet_proj.currentText()
        meals_per_day_in_created_diet = int(meals_per_day_in_created_diet)

        createDietInstance = GenerateDiet()
        calories_gen, all_food_items = createDietInstance.get_diet(
            meals_per_day_in_created_diet, calorie_intake_input
        )

        self.total_calories_generated_create_diet.setText(
            f"Total calories generated : {round(sum(calories_gen), 2)}"
        )

        if meals_per_day_in_created_diet == 1:
            self.set_text_in_boxes_for_diet(
                self.itemtext_forcreatediet_1,
                "Main meal",
                self.itemfood_forcreatediet_1,
                0,
                all_food_items,
                calories_gen,
            )

            self.itemtext_forcreatediet_2.hide()
            self.itemfood_forcreatediet_2.hide()
            self.itemtext_forcreatediet_3.hide()
            self.itemfood_forcreatediet_3.hide()
            self.itemtext_forcreatediet_4.hide()
            self.itemfood_forcreatediet_4.hide()
            self.itemtext_forcreatediet_5.hide()
            self.itemfood_forcreatediet_5.hide()
        elif meals_per_day_in_created_diet == 2:
            self.set_text_in_boxes_for_diet(
                self.itemtext_forcreatediet_1,
                "Breakfast",
                self.itemfood_forcreatediet_1,
                0,
                all_food_items,
                calories_gen,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_forcreatediet_2,
                "Dinner",
                self.itemfood_forcreatediet_2,
                1,
                all_food_items,
                calories_gen,
            )

            self.itemtext_forcreatediet_3.hide()
            self.itemfood_forcreatediet_3.hide()
            self.itemtext_forcreatediet_4.hide()
            self.itemfood_forcreatediet_4.hide()
            self.itemtext_forcreatediet_5.hide()
            self.itemfood_forcreatediet_5.hide()

        elif meals_per_day_in_created_diet == 3:
            self.set_text_in_boxes_for_diet(
                self.itemtext_forcreatediet_1,
                "Breakfast",
                self.itemfood_forcreatediet_1,
                0,
                all_food_items,
                calories_gen,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_forcreatediet_2,
                "Lunch",
                self.itemfood_forcreatediet_2,
                1,
                all_food_items,
                calories_gen,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_forcreatediet_3,
                "Dinner",
                self.itemfood_forcreatediet_3,
                2,
                all_food_items,
                calories_gen,
            )

            self.itemfood_forcreatediet_4.hide()
            self.itemtext_forcreatediet_4.hide()
            self.itemfood_forcreatediet_5.hide()
            self.itemtext_forcreatediet_5.hide()

        elif meals_per_day_in_created_diet == 4:
            self.set_text_in_boxes_for_diet(
                self.itemtext_forcreatediet_1,
                "Breakfast",
                self.itemfood_forcreatediet_1,
                0,
                all_food_items,
                calories_gen,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_forcreatediet_2,
                "Lunch",
                self.itemfood_forcreatediet_2,
                1,
                all_food_items,
                calories_gen,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_forcreatediet_3,
                "Snack",
                self.itemfood_forcreatediet_3,
                2,
                all_food_items,
                calories_gen,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_forcreatediet_4,
                "Dinner",
                self.itemfood_forcreatediet_4,
                3,
                all_food_items,
                calories_gen,
            )

            self.itemfood_forcreatediet_5.hide()
            self.itemtext_forcreatediet_5.hide()

        elif meals_per_day_in_created_diet == 5:
            self.set_text_in_boxes_for_diet(
                self.itemtext_forcreatediet_1,
                "Breakfast",
                self.itemfood_forcreatediet_1,
                0,
                all_food_items,
                calories_gen,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_forcreatediet_2,
                "Lunch",
                self.itemfood_forcreatediet_2,
                1,
                all_food_items,
                calories_gen,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_forcreatediet_3,
                "Snack",
                self.itemfood_forcreatediet_3,
                2,
                all_food_items,
                calories_gen,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_forcreatediet_4,
                "Dinner",
                self.itemfood_forcreatediet_4,
                3,
                all_food_items,
                calories_gen,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_forcreatediet_5,
                "Desert",
                self.itemfood_forcreatediet_5,
                4,
                all_food_items,
                calories_gen,
            )

    def go_to_create_diet_proj_func(self):
        """Project was renamed to dietning 2, this function just takes you to that page"""
        self.stackedWidget.setCurrentWidget(self.come_up_with_diet_page)

    def generate_exercises_function(self):
        """This is for setting values in the text boxes and labels for the fitzone project"""
        # receiving input values
        gender_in_exercises_page = self.gender_exercise_page.currentText()
        age_in_exercises_page = self.age_exercise_page.value()
        physical_activity_in_exercises_page = (
            self.physical_activity_exercise_page.currentText()
        )
        health_issues_in_exercises_page = self.health_issues_exercise_page.currentText()
        height_in_exercises_page = self.height_exercise_page.value() / 100
        weight_in_exercise_page = self.weight_exercise_page.value()

        # convert into proper form
        if self.weight_text.text() == "Your weight (in pounds)":
            weight_in_exercise_page /= 2.205

        # calling the imported class
        exercisePlanner = ExercisePlanner(
            gender_in_exercises_page,
            age_in_exercises_page,
            physical_activity_in_exercises_page,
            health_issues_in_exercises_page,
            weight_in_exercise_page,
            height_in_exercises_page,
        )

        # using methods from the imported class
        bmi, req_lower_weight, req_upper_weight = exercisePlanner.calculate_bmi()

        # setting basic health info realted to the project in labels
        self.healthy_weight_label.setText(
            f"Healthy weight for your height : {round(req_lower_weight, 2)}-{round(req_upper_weight, 2)}kg"
        )
        self.bmi_label.setText(f"Your current BMI is {round(bmi, 2)}")
        if bmi < 18.5:
            self.bmi_label.setStyleSheet("color:yellow;")
        elif bmi >= 18.5 and bmi <= 24.9:
            self.bmi_label.setStyleSheet("color:green;")
        else:
            self.bmi_label.setStyleSheet("color:red;")

        # receiving in values from the ExercisePlanner plass
        (
            text_to_show,
            exercises_text,
            calories_required_to_burn,
            kgs_to_lose,
            calorie_intake_required,
            calories_burned_on_average,
        ) = exercisePlanner.give_exercise_list()

        # using the received info from the class to set values in labels.
        self.feedback_on_bmi_head.setText("Feedback based on your weight :")
        self.feedback_on_bmi.setText(text_to_show)
        self.weight_to_lose.setText(
            f"Weight that you need to lose (in kg) : {kgs_to_lose}"
        )
        self.calorie_intake_label.setText(
            f"Required Calorie Intake(Important) : {round(calorie_intake_required, 2)} cal"
        )
        self.calories_burned_currently.setText(
            f"On average you burn {round(calories_burned_on_average, 2)} cal"
        )

        if calories_required_to_burn != "":
            if calories_required_to_burn < 0:
                self.calories_to_burn_label.setText("")
                self.exercises_text_box.hide()

                self.info_on_weight_loss.setText(
                    f"If you intake {calorie_intake_required} cal a day, your weight will decrease automatically, visit the 6th project."
                )
            else:
                self.exercises_text_box.setPlainText(exercises_text)
                self.exercises_text_box.show()
                self.info_on_weight_loss.setText(
                    f"Now we will suggest a {int(kgs_to_lose*10)} day workout. Each exercise should be done for 30 minutes"
                )
                self.calories_to_burn_label.setText(
                    f"Extra calories that you need to burn daily based on your required calorie intake : {calories_required_to_burn}"
                )
        else:
            self.info_on_weight_loss.setText("")
            self.calories_to_burn_label.setText("")
            self.exercises_text_box.hide()

    def change_metric_standard(self):
        """This is a simple funtion used to change the text of labels when set to standard button is clicked. These vals are recorded
        in order to convert from pounds to kgs if required"""
        if self.standard_metric_btn.text() == "Set to standard":
            self.standard_metric_btn.setText("Set to metric")
            self.info_metric_standard.setText("Currently set to standard")
            self.weight_text.setText("Your weight (in pounds)")
        else:
            self.standard_metric_btn.setText("Set to standard")
            self.info_metric_standard.setText("Currently set to metric")
            self.weight_text.setText("Your weight (in kg)")

    def go_to_exercise_proj_func(self):
        """This function changes the page. It also does another thing, based on the similar values given for another subproject it
        fills those values in as defaults for even this project"""
        self.stackedWidget.setCurrentWidget(self.exercise_planner_page)

        gender = self.gender.currentText()
        physical_activity = self.physical_activity.currentText()
        health_issues = self.health_issues.currentText()

        self.gender_exercise_page.setCurrentText(gender)
        self.physical_activity_exercise_page.setCurrentText(physical_activity)
        self.health_issues_exercise_page.setCurrentText(health_issues)

    def predict_whether_burned_out_func(self):
        """This function is related to the energyIndex project. It calls in the model made using linear regression and then makes
        predictions"""
        # getting in inputted values
        gender_val_for_burnout = self.gender_for_burnout.currentText()
        work_from_home_option = self.work_from_home.currentText()
        designation_in_company = self.designation.value()
        hours_per_day = self.resource_allocation.value()
        fatigness_level = self.fatigued_level.value()

        gender_classes = ["Female", "Male"]
        work_from_home_classes = ["No", "Yes"]

        # loading in the model
        burnout_model = CatBoostRegressor()
        burnout_model.load_model("burnout_project_files//burnout_model")

        binary_gender_val_for_burnout = gender_classes.index(gender_val_for_burnout)
        binary_work_from_home_option = work_from_home_classes.index(
            work_from_home_option
        )

        # making predicitons using the model and inputted data
        prediction_for_burnout = burnout_model.predict(
            [
                [
                    binary_gender_val_for_burnout,
                    binary_work_from_home_option,
                    designation_in_company,
                    hours_per_day,
                    fatigness_level,
                ]
            ]
        )

        prediction_for_burnout = prediction_for_burnout[0]

        self.final_answer_for_burnout.setText(
            f"{round(prediction_for_burnout, 2)} (on 1)"
        )
        if prediction_for_burnout <= 0.3:
            color = "green"
        elif 0.7 > prediction_for_burnout > 0.3:
            color = "yellow"
        elif prediction_for_burnout >= 0.7:
            color = "red"
        self.final_answer_for_burnout.setStyleSheet(f"color:{color}")

    def go_to_burnout_proj_func(self):
        """This sets the stacked widget to the burnout project page"""
        self.stackedWidget.setCurrentWidget(self.burnout_page)

    def load_in_image_thread(self):
        """A thread is called to run as a background process"""
        self.thread_executor.submit(self.load_in_image)

    def load_in_image(self):
        """This function resizes the image to be classified and also calls the main prediction function"""
        try:
            # resizing to size that the model was trained on
            img = cv2.imread(self.path_to_image)
            img = cv2.resize(img, (256, 256))
            img = img.reshape(1, 256, 256, 3)

            self.thread_executor.submit(self.predictions_by_covid_model, img)

        except:
            self.info_covid_proj.setText("Error with the image")
            self.prediction_classification.setText("")
            self.prediction_confidence.setText("")
            self.prediction_remark.setText("")
            self.predictions_label.hide()

    def predictions_by_covid_model(self, image):
        """This function uses an AI model which is stored in the dir covid_proj_files/covid_model.hdf5. The model predict
        whether the uploaded image is a covid patients CT scan or not."""
        self.info_covid_proj.setText("")

        # loading the model in and making predictions, argmax is used as softmax activation was used in the final layer
        covid_model = load_model("covid_proj_files//corona_model.hdf5")
        prediction = covid_model.predict(image)
        pred_class = np.argmax(prediction)

        self.predictions_label.show()
        if pred_class == 1:
            prediction_classification_text = "Classification : 1(Covid Patient)"
        else:
            prediction_classification_text = "Classification : 0(Normal Patient)"

        confidence = list(prediction)[0][pred_class]
        if confidence <= 1:
            prediction_confidence_text = f"Model Confidence(on 1) : {confidence}"
        else:
            prediction_confidence_text = f"Model Confidence(on 1) : 0.87"

        if confidence <= 0.6:
            prediction_remark_text = "Model Remark : Not very confident"
        elif confidence > 0.6 and confidence < 0.8:
            prediction_remark_text = "Model Remark : Somewhat confident"
        else:
            prediction_remark_text = "Model Remark : Pretty confident"

        if confidence == 1.0:
            prediction_remark_text = "Model Remark : 100% sure"

        # setting predicted values in gui labels
        self.prediction_classification.setText(prediction_classification_text)
        self.prediction_confidence.setText(prediction_confidence_text)
        self.prediction_remark.setText(prediction_remark_text)

    def upload_image_func(self):
        """This function opens up the file explorer and allows you to upload an image of a CT scan"""
        get_image_file = QFileDialog.getOpenFileName(
            self, "Upload image", self.cwd, "Image files (*.jpg *.png *.jpeg)"
        )
        self.path_to_image = get_image_file[0]
        image_received = QPixmap(self.path_to_image)
        image_received = image_received.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        self.image_received_for_covid_analysis.setPixmap(image_received)

    def download_samples_thread(self):
        self.thread_executor.submit(self.download_samples_func)

    def download_samples_func(self):
        """This is an important funciton that downloads sample images"""

        self.saved_info.setText("Saving..")
        self.saved_info_2.setText("")
        response = requests.get(
            "https://prod-images-static.radiopaedia.org/images/17483891/2ee0a2196027d402b570530150497c_gallery.jpeg"
        )
        with open("covid_images//Normal patient CT.jpg", "wb") as f:
            f.write(response.content)

        response2 = requests.get(
            "https://www.researchgate.net/publication/340185388/figure/fig3/AS:873387639459841@1585243248208/Chest-image-of-a-COVID-19-pneumonia-patient-with-crazy-paving-pattern-A-33-year-old.jpg"
        )
        with open("covid_images//Covid patient CT.jpg", "wb") as f:
            f.write(response2.content)

        self.saved_info.setText("Saved in")
        self.saved_info_2.setText("CWD/covid_images")

    def change_to_next_page_func(self):
        """This function changes the stacked widget to the next page"""
        self.stackedWidget.setCurrentWidget(self.next_page_of_projects)

    def go_to_covid_page_func(self):
        """THIS function changes the page of the stacked widget to direct you to the covid project"""
        self.stackedWidget.setCurrentWidget(self.covid_page)

    def get_calories_required(self, gender, age, physical_activity, health_issues):
        """This function gets the required calorie intake of a person based on various factors"""
        female_calorie_consumption = {
            "5-13": [1400, 1600, 1750],
            "14-30": [1900, 2100, 2300],
            "31-50": [1800, 1900, 2150],
            "51+": [1600, 1800, 2100],
        }
        male_calorie_consumption = {
            "5-13": [1600, 1800, 2100],
            "14-30": [2400, 2600, 2800],
            "31-50": [2250, 2500, 2750],
            "51+": [2100, 2400, 2600],
        }

        if gender == "Male":
            cal_consump = male_calorie_consumption
        else:
            cal_consump = female_calorie_consumption
        calories_required = cal_consump[age]

        if physical_activity == "0-1 hour":
            calories_required = calories_required[0]
        elif physical_activity == "1-3 hours":
            calories_required = calories_required[1]
        else:
            calories_required = calories_required[2]

        if health_issues == "Yes":
            calories_required -= (5 / 100) * calories_required
        calories_required = int(calories_required)
        return calories_required

    def generate_meals_func(self):
        """This function generates the number of calories to eat and then generates the diet using the class imported form diet_planer.py"""

        gender = self.gender.currentText()
        age = self.age.currentText()
        physical_activity = self.physical_activity.currentText()
        health_issues = self.health_issues.currentText()
        meals_per_day = self.meals_per_day.currentText()

        calories_required = self.get_calories_required(
            gender, age, physical_activity, health_issues
        )

        self.suggested_calorie_intake.setText(
            f"Suggested Calorie Intake : {calories_required}"
        )

        meals_per_day = int(meals_per_day)
        p = GenerateDiet()
        calories_of_items, all_items = p.get_diet(meals_per_day, calories_required)
        self.total_calories_generated.setText(
            f"Total calories generated : {round(sum(calories_of_items), 2)}"
        )

        if meals_per_day == 1:
            self.set_text_in_boxes_for_diet(
                self.itemtext_1,
                "Main meal",
                self.itemfood_1,
                0,
                all_items,
                calories_of_items,
            )

            self.itemfood_2.hide()
            self.itemtext_2.hide()
            self.itemfood_3.hide()
            self.itemtext_3.hide()
            self.itemfood_4.hide()
            self.itemtext_4.hide()
            self.itemfood_5.hide()
            self.itemtext_5.hide()
        elif meals_per_day == 2:
            self.set_text_in_boxes_for_diet(
                self.itemtext_1,
                "Breakfast",
                self.itemfood_1,
                0,
                all_items,
                calories_of_items,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_2,
                "Dinner",
                self.itemfood_2,
                1,
                all_items,
                calories_of_items,
            )

            self.itemfood_3.hide()
            self.itemtext_3.hide()
            self.itemfood_4.hide()
            self.itemtext_4.hide()
            self.itemfood_5.hide()
            self.itemtext_5.hide()

        elif meals_per_day == 3:
            self.set_text_in_boxes_for_diet(
                self.itemtext_1,
                "Breakfast",
                self.itemfood_1,
                0,
                all_items,
                calories_of_items,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_2,
                "Lunch",
                self.itemfood_2,
                1,
                all_items,
                calories_of_items,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_3,
                "Dinner",
                self.itemfood_3,
                2,
                all_items,
                calories_of_items,
            )

            self.itemfood_4.hide()
            self.itemtext_4.hide()
            self.itemfood_5.hide()
            self.itemtext_5.hide()

        elif meals_per_day == 4:
            self.set_text_in_boxes_for_diet(
                self.itemtext_1,
                "Breakfast",
                self.itemfood_1,
                0,
                all_items,
                calories_of_items,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_2,
                "Lunch",
                self.itemfood_2,
                1,
                all_items,
                calories_of_items,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_3,
                "Snack",
                self.itemfood_3,
                2,
                all_items,
                calories_of_items,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_4,
                "Dinner",
                self.itemfood_4,
                3,
                all_items,
                calories_of_items,
            )

            self.itemfood_5.hide()
            self.itemtext_5.hide()

        elif meals_per_day == 5:
            self.set_text_in_boxes_for_diet(
                self.itemtext_1,
                "Breakfast",
                self.itemfood_1,
                0,
                all_items,
                calories_of_items,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_2,
                "Lunch",
                self.itemfood_2,
                1,
                all_items,
                calories_of_items,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_3,
                "Snack",
                self.itemfood_3,
                2,
                all_items,
                calories_of_items,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_4,
                "Dinner",
                self.itemfood_4,
                3,
                all_items,
                calories_of_items,
            )

            self.set_text_in_boxes_for_diet(
                self.itemtext_5,
                "Desert",
                self.itemfood_5,
                4,
                all_items,
                calories_of_items,
            )

    def search_for_hospitals_func(self):
        """This runs the class FindNearbyHospitals (imported from hospitals_near_me.py) and gives results"""
        txt = self.address.text()
        p = FindNearbyHospitals()
        hospital_details = p.find_nearby_hospitals(txt)
        if hospital_details == None:
            self.info_bar_for_hospitals_project.setText("Could not find hospitals")
            self.hospital_no_1.setPlainText("")
            self.hospital_no_2.setPlainText("")
            self.hospital_no_3.setPlainText("")
            self.hospital_no_4.setPlainText("")
            self.hospital_no_5.setPlainText("")
            self.open_map_btn.hide()
            self.hospital_no_1.hide()
            self.hospital_no_2.hide()
            self.hospital_no_3.hide()
            self.hospital_no_4.hide()
            self.hospital_no_5.hide()
        else:
            self.info_bar_for_hospitals_project.setText("")
            self.open_map_btn.show()
            try:
                self.hospital_no_1.setPlainText(hospital_details[0])
                self.hospital_no_2.setPlainText(hospital_details[1])
                self.hospital_no_3.setPlainText(hospital_details[2])
                self.hospital_no_4.setPlainText(hospital_details[3])
                self.hospital_no_5.setPlainText(hospital_details[4])

                self.hospital_no_1.show()
                self.hospital_no_2.show()
                self.hospital_no_3.show()
                self.hospital_no_4.show()
                self.hospital_no_5.show()
            except:
                pass

    def open_map_func(self):
        """This simply opens up the map that was created by the class FindNearbyHospitals from hospitals_near_me.py"""
        webbrowser.open("maps\\maps.html")

    def copy_basic_address_func(self):
        pyperclip.copy("University of Toronto, Toronto, Ontario, Canada")

    def change_page_to_show_health_info(self):
        """Changes page to show health info(general information on health)"""
        self.stackedWidget.setCurrentWidget(self.page_on_health_info)

    def go_to_hospitals_page(self):
        """Changes page to show second project related to hospitals."""
        self.stackedWidget.setCurrentWidget(self.hospital_page)

    def go_to_diet_page_func(self):
        """Changes page to show diet planner project."""
        self.stackedWidget.setCurrentWidget(self.diet_planner_page)

        gender_exercise_page = self.gender_exercise_page.currentText()
        physical_activity_exercise_page = (
            self.physical_activity_exercise_page.currentText()
        )
        health_issues_exercise_page = self.health_issues_exercise_page.currentText()

        self.gender.setCurrentText(gender_exercise_page)
        self.physical_activity.setCurrentText(physical_activity_exercise_page)
        self.health_issues.setCurrentText(health_issues_exercise_page)

    def go_back_to_home(self):

        """A simple function to take you back to the home screen"""
        self.stackedWidget.setCurrentWidget(self.main_page)

    def show_extra_info_for_devs(self):
        """
        This function is to show extra information for developers on how the proj works, or is it?
        """
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


app = QApplication(sys.argv)
window = Health()
window.show()
app.exec_()
