# Premise: Mark sold 7 boxes less than n and Ann sold 2 boxes less than n.
# Hypothesis: Mark sold more than 6 boxes less than n and Ann sold 2 boxes less than n.
# Golden Label: entailment

boxes_mark_premise = 7
boxes_mark_hypothesis = 6
boxes_ann_premise = 2
boxes_ann_hypothesis = 2

# the hypothesis talks about the number of boxes sold by Mark and Ann, referenced also in the premise
if boxes_mark_hypothesis < boxes_mark_premise:
    # check if the hypothesis value contradicts the estimate of 'boxes_mark_premise' less than n
    label = "contradiction"
elif boxes_ann_hypothesis != boxes_ann_premise:
    # check if the number of boxes sold by Ann in the hypothesis contradicts the number of boxes sold by Ann in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

