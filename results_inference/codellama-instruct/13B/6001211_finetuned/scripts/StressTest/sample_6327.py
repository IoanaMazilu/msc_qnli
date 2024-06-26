boxes_per_minute_premise = 10
boxes_per_minute_hypothesis = 20

# the hypothesis refers to the number of boxes Kramer can pack per minute, mentioned in the premise
if boxes_per_minute_hypothesis <= boxes_per_minute_premise:
    # check if the hypothesis value contradicts the number of boxes Kramer can pack per minute in the premise
    label = "contradiction"
elif boxes_per_minute_premise > boxes_per_minute_hypothesis:
    # check if the number of boxes Kramer can pack per minute in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
