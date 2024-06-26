john_age_multiple_premise = 3
john_age_multiple_hypothesis = 3
time_past_premise = 6
time_past_hypothesis = 5

# the hypothesis refers to the age relation between John and Tom mentioned in the premise
if john_age_multiple_premise!= john_age_multiple_hypothesis:
    # check if the age multiple in the hypothesis contradicts the age multiple in the premise
    label = "contradiction"
elif time_past_hypothesis > time_past_premise:
    # check if the time in the past in the hypothesis contradicts the time in the past reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
