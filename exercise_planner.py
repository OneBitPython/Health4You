#                        INTUITION BEHIND THE CLASS
# calculate the numbmer of calories required by a person per day, then calculate the number of calories a normal
# person burns per day. Calculate the persons BMI and check their required weight to have a perfect BMI. If they have
# a perfect BMI then don't give them any difficult exercises or intense exercises. If there weight exceeds the upper limit
# of the weight for a perfect bmi then calculate the difference in the weight, based on this difference give them a schedule
# that creates a calorie deficit of 770 calories per day. This will allow them to reduce 1 kg in 10 days. The calorie deficit
# is the difference between the calories they require per day and (the calories they burn on average plus the calories they burn when doing exercises)

import random


class ExercisePlanner:
    def __init__(self, gender, age, physical_activity, health_issues, weight, height):
        # initializing a bunch of variables
        self.gender = gender
        self.age = age
        self.physical_activity = physical_activity
        self.health_issues = health_issues
        self.weight = weight  # weight in kg
        self.height = height  # height in metre
        self.lower_limit_bmi = 18.5
        self.upper_limit_bmi = 24.9

    def calculate_bmi(self):
        """This function calculates the bmi of the person using the formula kg/m**2, where m is the height in metre
        The function also calculates the weight range that you should be in based on your current height."""
        bmi = self.weight / (self.height ** 2)
        req_lower_weight = self.lower_limit_bmi * (
            self.height ** 2
        )  # simple transposition of the first formula
        req_upper_weight = self.upper_limit_bmi * (self.height ** 2)

        return bmi, req_lower_weight, req_upper_weight

    def give_exercise_list(self):
        """This function is a very important one. It first calulates the calories that you need to intake based on your age, gender
        physical activity and other factors. It then calculates the calories you burn on average using a formula. Finally it develops
        an exercise list based on your bmi"""

        from all_exercises import all_activities

        height_in_inches = self.height * 39.37  # convert metre to inches
        weight_in_pounds = self.weight * 2.205  # convert kg to pounds
        calorie_deficit_required_per_day = 770

        if self.age > 50:
            age_cat = "51+"
        elif self.age < 14:
            age_cat = "5-13"
        elif self.age >= 14 and self.age <= 30:
            age_cat = "14-30"
        elif self.age >= 31 and self.age <= 50:
            age_cat = "31-50"

        calories_required = self.get_calories_required(age_cat)
        bmi, req_lower_weight, req_upper_weight = self.calculate_bmi()

        exercises_text = "                             Exercises\n"
        calories_required_to_burn = ""
        if self.gender == "Male":
            calories_burned_on_average = (
                66
                + (6.2 * weight_in_pounds)
                + (12.7 * height_in_inches)
                - (6.76 * self.age)
            )  # formula used can be found at : https://www.medicalnewstoday.com/articles/319731#calculating-how-many-calories-are-burned-in-a-day
        else:
            calories_burned_on_average = (
                655.1
                + (4.35 * weight_in_pounds)
                + (4.7 * height_in_inches)
                - (4.7 * self.age)
            )

        if self.physical_activity == "0-1 hour":
            calories_burned_on_average *= 1.2
        elif self.physical_activity == "1-3 hours":
            calories_burned_on_average *= 1.3
        elif self.physical_activity == "3+ hours":
            calories_burned_on_average *= 1.5

        mean_weight = (req_lower_weight + req_upper_weight) / 2
        if self.weight < req_lower_weight:
            kgs_to_lose = 0  # this shows that the weight or bmi is too low, ie they are underweight
            text_to_show = "Your weight is too low, check out the diet planner project. We recommend some light exercises."
        elif self.weight < req_upper_weight:
            kgs_to_lose = 0  # their weight is alright ie bmi is alright
            text_to_show = f"Looks like your BMI is alright, we suggest some basic exercise like {random.choice(list(all_activities.keys()))}"

        else:
            text_to_show = "Looks like your weight is above the required level"
            kgs_to_lose = self.weight - mean_weight
            kgs_to_lose = round(kgs_to_lose, 2)

            calories_required_to_burn = (
                calories_required - calories_burned_on_average
            ) + 770  # this 770 is the calorie deficity required per day to lose 1kg in 10 days. Calorie deficit can also be stated as
            # the difference between your calorie intake adn teh calories that you burn.
            calories_required_to_burn = round(calories_required_to_burn, 2)

            weight_cat = [125, 155, 185]
            min_val = min(
                weight_cat, key=lambda x: abs(x - weight_in_pounds)
            )  # this is done because calories burned are different
            # for different weights
            min_idx = weight_cat.index(min_val)

            shuffled = list(
                all_activities.items()
            )  # shuffling all activities to get unique values each and every time
            random.shuffle(shuffled)
            all_activities = dict(shuffled)

            calories_burned_total = 0
            for exercise in all_activities:
                cal_burned = all_activities[exercise][min_idx]
                if calories_burned_total + cal_burned < calories_required_to_burn + 25:
                    exercises_text += f"{exercise} : {cal_burned} cal burned\n"
                    calories_burned_total += cal_burned

                if calories_burned_total >= calories_required_to_burn:
                    break
            exercises_text += f"Calories burned in total : {calories_burned_total} cal"
        return (
            text_to_show,  # info on their weight and bmi
            exercises_text,  # exercises if their bmi exceeds 25
            calories_required_to_burn,  # extra calories that they need to burn daily
            kgs_to_lose,
            calories_required,  # calorie intake that should be adhered to
            calories_burned_on_average,  # calories burned on an average day(without provided or suggested exercises)
        )  # these are all the values that are returned so that they can be displayed in the main GUI

    def get_calories_required(self, age):
        """Uses a simple table that was scraped to get the required calorie intake to stay healthy"""

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

        if self.gender == "Male":
            cal_consump = male_calorie_consumption
        else:
            cal_consump = female_calorie_consumption
        calories_required = cal_consump[age]

        if self.physical_activity == "0-1 hour":
            calories_required = calories_required[0]
        elif self.physical_activity == "1-3 hours":
            calories_required = calories_required[1]
        else:
            calories_required = calories_required[2]

        if self.health_issues == "Yes":
            calories_required -= (
                5 / 100
            ) * calories_required  # reduces 5% of calories if they have health issues
        calories_required = int(calories_required)
        return calories_required
