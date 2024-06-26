years_future_premise = 18
years_future_hypothesis = 88

# the hypothesis refers to Molly's future age, which is also mentioned in the premise
if years_future_hypothesis < years_future_premise:
    # check if the estimate of 'years_future_hypothesis' contradicts the number of future years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
