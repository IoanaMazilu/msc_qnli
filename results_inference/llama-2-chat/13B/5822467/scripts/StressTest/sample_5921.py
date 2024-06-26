home_to_beach_speed_premise = 80
home_to_beach_speed_hypothesis = 85
beach_to_home_speed_premise = 70

# define variables with representative names for the numerical entities in both inputs

# extract all quantities as valid numbers (integers or floats)

# compare the variables to infer one of the following labels:
# entailment, contradiction, neutral

if home_to_beach_speed_hypothesis > home_to_beach_speed_premise:
    # the hypothesis refers to the average speed of driving from home to the beach
    label = "entailment"
elif beach_to_home_speed_premise!= beach_to_home_speed_hypothesis:
    # the hypothesis refers to the average speed of driving from the beach to home
    label = "contradiction"
else:
    # the premise and hypothesis values are consistent, no conclusion can be drawn
    label = "neutral"

print(label)
