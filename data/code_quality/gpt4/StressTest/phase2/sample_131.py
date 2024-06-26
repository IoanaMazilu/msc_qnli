john_age_past_premise = 3
john_age_past_hypothesis = 3
time_past_premise = 6
time_past_hypothesis = 1

# the hypothesis talks about the age relation between John and Tom at a certain point in the past, which is also referenced in the premise
if john_age_past_hypothesis != john_age_past_premise:
    # check if the age ratio in the hypothesis contradicts the age ratio provided in the premise
    label = "contradiction"
elif time_past_hypothesis != time_past_premise:
    # check if the time in the past mentioned in the hypothesis contradicts the time in the past mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
