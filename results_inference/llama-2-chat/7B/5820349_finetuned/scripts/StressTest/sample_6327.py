boxes_packed_premise = 10
boxes_packed_hypothesis = 20

# the hypothesis refers to the number of boxes of cigarettes Kramer can pack per minute, mentioned in the premise
if boxes_packed_premise >= boxes_packed_hypothesis:
    # check if the estimate of 'boxes_packed_hypothesis' contradicts the number of boxes packed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
