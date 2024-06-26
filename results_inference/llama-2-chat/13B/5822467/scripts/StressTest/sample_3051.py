premise_time = 3
hypothesis_time = 1

# the hypothesis refers to the duration of the bike ride, mentioned in the premise
if premise_time <= hypothesis_time:
    # check if the estimate of 'hypothesis_time' contradicts the duration of the bike ride in the premise
    label = "contradiction"
elif hypothesis_time > premise_time:
    # the hypothesis value is greater than the premise value, so it cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
