boxes_packed_premise = 20
boxes_packed_hypothesis = 10

# the hypothesis refers to the number of boxes Kramer can pack per minute, which is also mentioned in the premise
if boxes_packed_hypothesis >= boxes_packed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'boxes_packed_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise estimate, we can infer entailment
    label = "entailment"

print(label)
