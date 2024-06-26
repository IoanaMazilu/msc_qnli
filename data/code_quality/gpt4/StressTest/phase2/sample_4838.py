karen_speed_premise = 60
karen_speed_hypothesis = 60
tom_speed_premise = 45
tom_speed_hypothesis = 45

# the hypothesis refers to the speed at which Karen and Tom are driving, mentioned in the premise
if karen_speed_hypothesis >= karen_speed_premise:
    # check if Karen's speed in the hypothesis contradicts Karen's speed in the premise
    label = "contradiction"
elif tom_speed_hypothesis != tom_speed_premise:
    # check if Tom's speed in the hypothesis contradicts Tom's speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
