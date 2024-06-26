sold_value_premise = 450
sold_value_hypothesis = 750

# the hypothesis refers to the value of something sold, also mentioned in the premise
if sold_value_premise >= sold_value_hypothesis:
    # check if the value in the premise contradicts the estimate of less than'sold_value_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
