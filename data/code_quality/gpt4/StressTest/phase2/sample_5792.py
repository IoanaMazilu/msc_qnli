karen_speed_premise = 60
tom_speed_premise = 45
karen_speed_hypothesis = 59.99999999999999 # This is less than 60
tom_speed_hypothesis = 45

# the hypothesis refers to Karen and Tom's driving speeds mentioned in the premise
if karen_speed_hypothesis > karen_speed_premise:
    # check if the hypothesis value for Karen's speed contradicts the premise
    label = "contradiction"
elif tom_speed_hypothesis != tom_speed_premise:
    # check if the hypothesis value for Tom's speed contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
