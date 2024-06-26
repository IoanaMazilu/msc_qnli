boxes_sold_premise = 7
boxes_sold_hypothesis = 6

# the hypothesis refers to the number of boxes sold by Mark and Ann, mentioned in the premise
if boxes_sold_premise <= boxes_sold_hypothesis:
    # check if the estimate of 'boxes_sold_hypothesis' contradicts the number of boxes sold by Mark in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
