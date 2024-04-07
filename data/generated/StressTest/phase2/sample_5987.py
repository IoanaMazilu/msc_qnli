# Premise: Mark sold 6 boxes less than n and Ann sold 2 boxes less than n.
# Hypothesis: Mark sold less than 6 boxes less than n and Ann sold 2 boxes less than n.
# Golden Label: contradiction

boxes_mark_premise = 6
boxes_mark_hypothesis = 6
boxes_ann_premise = 2
boxes_ann_hypothesis = 2

# the hypothesis refers to the number of boxes sold by Mark and Ann in relation to 'n', also mentioned in the premise
if boxes_mark_hypothesis >= boxes_mark_premise:
    # check if the hypothesis value contradicts the premise about the number of boxes sold by Mark
    label = "contradiction"
elif boxes_ann_hypothesis != boxes_ann_premise:
    # check if the number of boxes sold by Ann in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

