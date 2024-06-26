fastest_horses_premise = 4
fastest_horses_hypothesis = 3
total_horses_premise = 25
total_horses_hypothesis = 25

# the hypothesis refers to the number of fastest horses and total horses mentioned in the premise
if fastest_horses_hypothesis >= fastest_horses_premise:
    # check if the estimate of 'fastest_horses_hypothesis' contradicts the number of fastest horses in the premise
    label = "contradiction"
elif total_horses_hypothesis!= total_horses_premise:
    # check if the number of total horses in the hypothesis contradicts the number of total horses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
