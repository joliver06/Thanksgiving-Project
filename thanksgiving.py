weight = 0


print("Hey! Welcome to the Turkey Cooking Time Calculator!")


while True:
    weight_input = input("How heavy is your turkey in pounds: ")


    if weight_input.isdigit():
        weight = float(weight_input)
        if weight > 0:
            break
        else:
            print("Enter a valid input. The weight should be greater than 0.")
    else:
        print("Oops! That doesn't look like a number. Please enter the weight as a number.")


cook_time = weight * 15


print("For a " + str(weight) + "-pound turkey, it should take about " + str(cook_time) + " minutes to cook.")





















