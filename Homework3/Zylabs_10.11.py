# ZyLabs 10.11
# Benjamin Ojode
# 1663352

class FoodItem:
    def __init__(self, name = "None", fat = 0.0, carbs = 0.0, protein = 0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

if __name__ == "__main__":
    initial_food = FoodItem()
    food_name = input()
    food_fat = float(input())
    food_carbs = float(input())
    food_protein = float(input())

    initial_food_2 = FoodItem(food_name, food_fat, food_carbs, food_protein)
    num_servings = float(input())

    initial_food.print_info()
    print(f'Number of calories for {num_servings:.2f} serving(s): {initial_food.get_calories(1):.2f}')
    print()

    initial_food_2.print_info()
    print(f'Number of calories for {num_servings:.2f} serving(s): {initial_food_2.get_calories(1):.2f}')