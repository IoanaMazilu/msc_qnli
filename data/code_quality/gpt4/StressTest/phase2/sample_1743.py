return_premise = 4
return_hypothesis = 2

# the hypothesis refers to the return on investment after 'n' years mentioned in the premise
if return_hypothesis >= return_premise:
    # check if the estimate of 'return_hypothesis' contradicts the return on investment in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
