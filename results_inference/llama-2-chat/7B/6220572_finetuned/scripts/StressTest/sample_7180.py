driven_hr_premise = 5
driven_hr_hypothesis = 1
driven_speed_premise = 42
driven_speed_hypothesis = 42
driven_time_premise = 3
driven_time_hypothesis = 3

# the hypothesis talks about the number of hours and speeds Andrew drove in the premise
if driven_hr_hypothesis!= driven_hr_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
elif driven_speed_hypothesis!= driven_speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif driven_time_hypothesis!= driven_time_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
