return_premise = 2
return_hypothesis = 3

# the hypothesis refers to the return on investment after 'n' years mentioned in the premise
if return_hypothesis <= return_premise:
    # check if the estimate of'return_hypothesis' contradicts the return on investment in the premise
    label = "contradiction"
elif return_premise >= return_hypothesis:
    # check if the return on investment in the premise contradicts the estimate of'return_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
