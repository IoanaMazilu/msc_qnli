bottles_premise = 45
drunk_bottles_premise = 14
left_bottles_hypothesis = 18

# the hypothesis talks about the number of bottles left, which is also referenced in the premise
if left_bottles_hypothesis!= bottles_premise - drunk_bottles_premise:
    # check if the number of bottles left in the hypothesis contradicts the number of bottles left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
