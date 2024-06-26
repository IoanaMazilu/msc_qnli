fastest_horses_premise = 3
fastest_horses_hypothesis = 4
total_horses = 25

# the hypothesis refers to the number of fastest horses mentioned in the premise
if fastest_horses_premise >= fastest_horses_hypothesis:
    # check if the estimate of 'fastest_horses_hypothesis' contradicts the number of fastest horses in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
