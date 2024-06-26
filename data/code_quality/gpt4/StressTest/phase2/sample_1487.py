average_mark_difference_premise = 17
average_mark_difference_hypothesis = 17

# the hypothesis refers to the average mark difference mentioned in the premise
if average_mark_difference_premise != average_mark_difference_hypothesis:
    # check if the average mark difference in the hypothesis contradicts the average mark difference reported in the premise
    label = "contradiction"
else:
    # if the average mark difference in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
