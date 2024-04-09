# Define variables with representative names for the numerical entities in both inputs
percentage_samsung_premise = 25
percentage_iphone_premise = 70
percentage_samsung_hypothesis = 75
percentage_iphone_hypothesis = 70

# Extract all quantities as valid numbers (integers or floats)
percentage_samsung_premise = int(percentage_samsung_premise)
percentage_iphone_premise = int(percentage_iphone_premise)
percentage_samsung_hypothesis = int(percentage_samsung_hypothesis)
percentage_iphone_hypothesis = int(percentage_iphone_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
# Do not use their values in the comments

# Check if the hypothesis values and estimates do not contradict the premise ones
# If so, we can infer entailment
if percentage_samsung_hypothesis <= percentage_samsung_premise and percentage_iphone_hypothesis <= percentage_iphone_premise:
    label = "entailment"

# Check if the estimate of 'percentage_samsung_hypothesis' contradicts the number of Samsung phone users in the premise
elif percentage_samsung_hypothesis > percentage_samsung_premise:
    label = "contradiction"

# Check if the number of iPhone users in the hypothesis contradicts the number of iPhone users reported in the premise
elif percentage_iphone_hypothesis!= percentage_iphone_premise:
    label = "contradiction"

else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
