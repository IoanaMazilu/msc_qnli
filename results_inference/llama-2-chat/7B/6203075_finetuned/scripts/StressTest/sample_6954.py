average_shirts_premise = 40
average_shirts_hypothesis = 80
shirts_purchased_premise = 8
shirts_purchased_hypothesis = 8

# the hypothesis refers to the average number of shirts each person has after purchasing 8 shirts each
if average_shirts_hypothesis < average_shirts_premise:
    # check if the hypothesis value contradicts the premise value of 'average_shirts_premise'
    label = "contradiction"
elif shirts_purchased_hypothesis!= shirts_purchased_premise:
    # check if the number of shirts purchased in the hypothesis contradicts the number of shirts purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
