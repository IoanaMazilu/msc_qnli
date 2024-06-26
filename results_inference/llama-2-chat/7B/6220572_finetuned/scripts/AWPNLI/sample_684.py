bottles_premise = 45
bottles_left_hypothesis = 23

# compute the number of bottles left in the premise
bottles_left_premise = bottles_premise - (bottles_premise / 2)

if bottles_left_hypothesis!= bottles_left_premise:
    # check if the number of bottles left in the hypothesis contradicts the number of bottles left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
