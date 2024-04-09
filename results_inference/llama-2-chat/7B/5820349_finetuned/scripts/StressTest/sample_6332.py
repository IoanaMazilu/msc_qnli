boxes_premise = 5
boxes_hypothesis = 1

# the hypothesis talks about the number of boxes in a case, referenced also in the premise
if boxes_hypothesis!= boxes_premise:
    # check if the number of boxes in the hypothesis contradicts the number of boxes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
