average_shirts_premise = 40
average_shirts_hypothesis = 80
shirts_purchased_premise = 8
shirts_purchased_hypothesis = 8

# the hypothesis refers to the average number of shirts each person has after purchasing, which is also mentioned in the premise
if average_shirts_hypothesis <= average_shirts_premise:
    # check if the hypothesis value contradicts the premise value of 'average_shirts_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
