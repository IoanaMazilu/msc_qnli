ages_sum_future_premise = 51
ages_sum_future_hypothesis = 51

# the hypothesis refers to the sum of ages in the future mentioned in the premise
if ages_sum_future_hypothesis > ages_sum_future_premise:
    # check if the estimate of 'ages_sum_future_hypothesis' contradicts the sum of ages in the future given in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
