driving_hours_premise = 9
driving_hours_hypothesis = 9
driving_speed_premise = 60
driving_speed_hypothesis = 60

# the hypothesis refers to the hours of driving and speed mentioned in the premise
if driving_hours_hypothesis > driving_hours_premise:
    # check if the hypothesis value contradicts the hours of driving stated in the premise
    label = "contradiction"
elif driving_speed_hypothesis != driving_speed_premise:
    # check if the speed of driving in the hypothesis contradicts the speed of driving stated in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
