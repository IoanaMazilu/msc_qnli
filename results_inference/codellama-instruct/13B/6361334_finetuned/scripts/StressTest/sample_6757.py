tom_goes_after_premise = 4
tom_goes_after_hypothesis = 8

# the hypothesis refers to the number of P that Tom goes after, mentioned in the premise
if tom_goes_after_hypothesis <= tom_goes_after_premise:
    # check if the estimate of 'tom_goes_after_hypothesis' contradicts the number of P in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
