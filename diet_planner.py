import random
from all_food_items import *


class GenerateDiet:
    def __init__(self):
        pass

    def shuffle_vals(self, dict_):
        """This shuffles a dictionary that is given to it, this is so a new list of food items can be provided each and every time"""
        l = list(dict_.items())
        random.shuffle(l)
        dict_ = dict(l)
        return dict_

    def get__item_list(self, calories, dict_):
        """This is the function that generates the list of food items to eat. It takes in the calories and then loops through
        the values of a dictionary which contains a lsit of food items, see "all_food_items.py". It then uses a simple algorithm
        to get as close to the required calories as possible while also producing unique diets each time"""
        total_cals = 0
        items_added = []

        dict_ = self.shuffle_vals(
            dict_
        )  # shuffling the dicitonary to keep a unique order
        for i in dict_:
            cal_of_item = dict_[i]
            if (
                total_cals + cal_of_item <= calories + 20
            ):  # checking calories added in the diet
                items_added.append([i, cal_of_item])
                total_cals += cal_of_item
            else:
                pass
            if total_cals >= calories:
                break

        calories_generated = 0
        list_of_items = []
        for i in items_added:
            list_of_items.append(i)
            calories_generated += dict_[i[0]]
        return calories_generated, list_of_items

    def get_diet(self, meals, calories):
        """This function takes in meals and total calories to intake and generates different sets of meals ie breakfast
        lunch, snacks, dinner and desert. The idea is a person who wants two meals will get dinner and breakfast, the person
        who wants 3 meals will get breakfast lunch and dinner and so on..."""
        if meals == 1:
            calories_gen_dinner, list_of_dinner_items = self.get__item_list(
                calories, dinner_dict
            )

            all_items = [list_of_dinner_items]
            calories_gen_altogether = [calories_gen_dinner]
            return calories_gen_altogether, all_items

        elif meals == 2:
            breakfast_cal = (
                60 / 100
            ) * calories  # splitting calories that need to be eaten for breakfast and dinner
            dinner_cal = (
                40 / 100
            ) * calories  # 60% calories for breakfast and 40% for dinner

            calories_gen_breakfast, list_of_breakfast_items = self.get__item_list(
                breakfast_cal, breakfast_dict
            )
            calories_gen_dinner, list_of_dinner_items = self.get__item_list(
                dinner_cal, dinner_dict
            )

            all_items = [list_of_breakfast_items, list_of_dinner_items]
            calories_gen_altogether = [calories_gen_breakfast, calories_gen_dinner]
            return calories_gen_altogether, all_items

        elif meals == 3:
            breakfast_cal = (40 / 100) * calories
            lunch_cal = (30 / 100) * calories
            dinner_cal = (30 / 100) * calories

            calories_gen_breakfast, list_of_breakfast_items = self.get__item_list(
                breakfast_cal, breakfast_dict
            )
            calories_gen_lunch, list_of_lunch_items = self.get__item_list(
                lunch_cal, lunch_dict
            )
            calories_gen_dinner, list_of_dinner_items = self.get__item_list(
                dinner_cal, dinner_dict
            )

            all_items = [
                list_of_breakfast_items,
                list_of_lunch_items,
                list_of_dinner_items,
            ]
            calories_gen_altogether = [
                calories_gen_breakfast,
                calories_gen_lunch,
                calories_gen_dinner,
            ]
            return calories_gen_altogether, all_items

        elif meals == 4:
            breakfast_cal = (40 / 100) * calories
            lunch_cal = (30 / 100) * calories
            dinner_cal = (20 / 100) * calories
            snack_cal = (10 / 100) * calories

            calories_gen_breakfast, list_of_breakfast_items = self.get__item_list(
                breakfast_cal, breakfast_dict
            )
            calories_gen_lunch, list_of_lunch_items = self.get__item_list(
                lunch_cal, lunch_dict
            )
            calories_gen_snack, list_of_snack_items = self.get__item_list(
                snack_cal, snack_dict
            )
            calories_gen_dinner, list_of_dinner_items = self.get__item_list(
                dinner_cal, dinner_dict
            )

            all_items = [
                list_of_breakfast_items,
                list_of_lunch_items,
                list_of_snack_items,
                list_of_dinner_items,
            ]
            calories_gen_altogether = [
                calories_gen_breakfast,
                calories_gen_lunch,
                calories_gen_snack,
                calories_gen_dinner,
            ]
            return calories_gen_altogether, all_items

        elif meals == 5:
            breakfast_cal = (30 / 100) * calories
            lunch_cal = (23 / 100) * calories
            dinner_cal = (22 / 100) * calories
            snack_cal = (10 / 100) * calories
            desert_cal = (15 / 100) * calories

            calories_gen_breakfast, list_of_breakfast_items = self.get__item_list(
                breakfast_cal, breakfast_dict
            )
            calories_gen_lunch, list_of_lunch_items = self.get__item_list(
                lunch_cal, lunch_dict
            )
            calories_gen_snack, list_of_snack_items = self.get__item_list(
                snack_cal, snack_dict
            )
            calories_gen_dinner, list_of_dinner_items = self.get__item_list(
                dinner_cal, dinner_dict
            )
            calories_gen_desert, list_of_desert_items = self.get__item_list(
                desert_cal, desert_dict
            )

            all_items = [
                list_of_breakfast_items,
                list_of_lunch_items,
                list_of_snack_items,
                list_of_dinner_items,
                list_of_desert_items,
            ]
            calories_gen_altogether = [
                calories_gen_breakfast,
                calories_gen_lunch,
                calories_gen_snack,
                calories_gen_dinner,
                calories_gen_desert,
            ]
            return calories_gen_altogether, all_items
