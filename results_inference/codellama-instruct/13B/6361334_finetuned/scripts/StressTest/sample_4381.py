hours_at_50_premise = 8
hours_at_50_hypothesis = 1
hours_at_60_premise = 3
hours_at_60_hypothesis = 3

# the hypothesis refers to the number of hours at 50 mph and 60 mph, mentioned in the premise
if hours_at_50_hypothesis > hours_at_50_premise:
    # check if the estimate of 'hours_at_50_hypothesis' contradicts the number of hours at 50 mph in the premise
    label = "contradiction"
elif hours_at_60_hypothesis!= hours_at_60_premise:
    # check if the number of hours at 60 mph in the hypothesis contradicts the number of hours at 60 mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
