boxes_per_minute_premise = 10
boxes_per_minute_hypothesis = 20

# the hypothesis refers to the number of boxes Kramer can pack per minute, which is also mentioned in the premise
if boxes_per_minute_premise >= boxes_per_minute_hypothesis:
    # check if the number of boxes Kramer can pack per minute in the premise contradicts the hypothesis estimate of less than 'boxes_per_minute_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
