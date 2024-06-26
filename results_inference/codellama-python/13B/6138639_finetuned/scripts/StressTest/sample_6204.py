purchased_premise = 20
purchased_hypothesis = 60

# the hypothesis refers to the number of items purchased from Ram by Mohan, mentioned in the premise
if purchased_hypothesis <= purchased_premise:
    # check if the estimate of 'purchased_hypothesis' contradicts the number of items purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
