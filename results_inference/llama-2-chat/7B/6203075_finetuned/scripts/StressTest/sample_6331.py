boxes_premise = 8
boxes_hypothesis = 5
time_premise = 2
time_hypothesis = 2

# the hypothesis refers to the number of boxes in one case, which is also mentioned in the premise
if boxes_hypothesis >= boxes_premise:
    # check if the number of boxes in the hypothesis contradicts the estimate of less than 'boxes_premise'
    label = "contradiction"
elif boxes_hypothesis < boxes_premise:
    # the premise gives only an estimate for the number of boxes
    # any number of boxes less than 'boxes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
