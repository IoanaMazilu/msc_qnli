premise_days = 7
hypothesis_days = 8

# the hypothesis refers to the number of days Ben worked before being joined by Blake
if premise_days <= hypothesis_days:
    # check if the estimate of 'hypothesis_days' contradicts the number of days Ben worked in the premise
    label = "contradiction"
elif hypothesis_days!= premise_days:
    # check if the number of days Ben worked in the hypothesis contradicts the number of days Ben worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
