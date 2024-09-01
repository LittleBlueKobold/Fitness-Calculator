#How to Determine your BMR (Basil Metabolic Rate) and TDE (Total Daily Expenditure)


#Calorie Calculation
def calorie_equation_male(weight_kg, height_cm, age):
     return ((10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5)

def calorie_equation_female(weight_kg, height_cm, age):
    return ((10 * weight_kg) + (6.25 * height_cm) -(5 * age) - 161)

#Enter Male or Female
sex = ["male", "female"]

#activity level selection

activity_levels = {
    "sedentary": 1.2,
    "lightly active": 1.375,
    "moderately active": 1.55,
    "active": 1.725,
    "very active": 1.9,
}

#Calculating Basil Metabolic Rate (BMR)
while True:
     try:
        MF=input("Please enter whether you are Male or Female and press Enter:").lower()
        if MF not in sex:
            raise ValueError("Invalid input! Please type 'male' or 'female'.")
        
        #Get and validate numeric inputs
        if MF in sex:
            print(f"Thank you, you have entered {MF}.")
            input("Please press enter to continue....")

            #weight calculation and verification
            try:
                weight = float(input("Please enter your weight in lbs:"))
            except:
                raise ValueError("Please enter using your weight using only numbers.")
            weight_kg = round(weight / 2.2046, 2)
            print (f"Your weight is", weight,"which is equal to", weight_kg, "in Kiligrams.")
            input("Please press enter to continue....")

            #height calculation and verification
            try:
                height = float(input("Please enter your height in inches:"))
            except:
                raise ValueError("Please enter your height using only numbers and in inches.")
            height_cm = (height * 2.54)
            print(f"you entered:", height, "which converts to:", height_cm, "in centimeters.")
            input("Please press enter to continue....")

            #age input
            try:
                age = int(input("Please enter your age in years:"))
            except:
                raise ValueError("please enter your age using only numbers!")


        #Get and validate activity level
        activity = input("Enter your activity level (sedentary, lightly active, moderately active, active, very active): ").lower()
        if activity not in activity_levels:
            raise ValueError("Sorry. Please enter one of the following: sedentary, lightly active, moderately active, active, very active")
        
        #calculate base calories
        if MF == 'male':
            calories = calorie_equation_male(weight_kg, height_cm, age)

        else:
            calories = calorie_equation_female(weight_kg, height_cm, age)
        
        #adjust calories based on activity level
        calories *= activity_levels[activity]

        #Total Daily Expenditure calculation

        #return total calorie needs of user
        print(f"Thank you for using this calorie calculator!",
              "You have entered ", {weight_kg}, "for your weight", {height_cm}, "for your height and", age, "as your age")
        print(f"The amount of calories you need each day to sustain your weight is ", {calories}, (input()))

        #how we came to this number for calories based on male or female
        print(f"we got this number using the following equation: ")

        if MF == 'male':
            print(f"((10 x weight in kg) + (6.25 x height in cm) - (5 x age) + 5) x activity level")
            print(f"Base calories: {(10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5} x activity level")
            print(f"Total calories: {calories:.2f}")
        else:
            print(f"((10 x weight in kg) + (6.25 x height in cm) - (5 x age) - 161) x activity level")
            print(f"Base calories: {(10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161} x activity level")
            print(f"Total calories: {calories:.2f}")

        print("Now, lets calculate your Macronutrient requirements! Press Enter to continue!")
        input()
     
        #Now we calculate Macronutrients to meet calorie goal

        #calculate each macronutrient in grams
        weightloss_calories = calories * 0.8
        print("in order to lose weight, you need to maintain a daily calorie intake of: ", weightloss_calories)
        input("Press enter to continue")
        protein = round(weight_kg * 1.2, 2)
        fats = round((weightloss_calories * 0.20) / 9, 2)
        carbs = round((weightloss_calories - ((protein * 4) + (fats * 9))) /4, 2)

        print(f"now to calculate your macronutrient requirements 'bEeP bOoP BeEp BoOp")
        print(f"your daily needs are: ", protein, "grams of protein", carbs, "grams of carbs and", fats, "grams of fats")

        break
     
     
     except ValueError as e:
        print(e)
        print("Lets try that again.")