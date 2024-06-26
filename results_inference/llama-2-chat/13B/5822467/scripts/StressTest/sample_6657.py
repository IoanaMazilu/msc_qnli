# Define variables with representative names for the numerical entities in both inputs
karen_speed_premise = 60
tom_speed_premise = 45
karen_speed_hypothesis = 80
q_miles_premise = None

# Extract all quantities as valid numbers
try:
    q_miles_hypothesis = float(input("Enter the number of Q miles Tom will drive before Karen wins the bet: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    q_miles_hypothesis = None

# Compare the variables
if karen_speed_hypothesis > karen_speed_premise:
    # The hypothesis contradicts the premise
    label = "contradiction"
elif q_miles_hypothesis > q_miles_premise:
    # The hypothesis entails the premise
    label = "entailment"
else:
    # The premise and hypothesis are neutral
    label = "neutral"

print(label)
