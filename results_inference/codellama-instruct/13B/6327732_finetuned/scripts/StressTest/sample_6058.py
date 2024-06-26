anita_days = 18
indu_days = 27
geeta_days = 36

# the hypothesis refers to the number of days mentioned in the premise
if anita_days <= anita_days:
    # check if the estimate of 'anita_days' contradicts the number of days in the premise
    label = "contradiction"
elif indu_days!= indu_days:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif geeta_days!= geeta_days:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
