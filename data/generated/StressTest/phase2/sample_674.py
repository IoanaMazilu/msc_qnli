# Premise: Jake drives at a constant speed of 29 km per hour.
# Hypothesis: Jake drives at a constant speed of more than 29 km per hour.
# Golden Label: contradiction

speed_premise = 29
speed_hypothesis = 29

# the hypothesis refers to the speed of Jake's driving mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the speed of Jake's driving in the premise
    label = "contradiction"
else:
    # the premise gives the exact speed of Jake's driving
    # any speed higher than 'speed_premise' is not consistent with the premise, therefore it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

