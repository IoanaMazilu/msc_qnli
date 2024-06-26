home_to_beach_speed_premise = 40
home_to_beach_speed_hypothesis = 80
return_home_speed_premise = 70

# define variables with representative names for the numerical entities in both inputs

# extract all quantities as valid numbers (integers or floats)

# compare the variables to determine the label
if home_to_beach_speed_hypothesis <= home_to_beach_speed_premise:
    # check if the estimate of 'home_to_beach_speed_hypothesis' contradicts the speed reported in the premise
    label = "contradiction"
elif return_home_speed_premise!= return_home_speed_hypothesis:
    # check if the speed reported in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
