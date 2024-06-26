# the premise gives the time period Rick invested his amount, and the hypothesis gives a different time period
if premise_time_premise > hypothesis_time_hypothesis:
    # check if the time period in the hypothesis contradicts the time period reported in the premise
    label = "contradiction"
elif hypothesis_time_hypothesis >= 7:
    # check if the time period in the hypothesis is consistent with the premise estimate
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
