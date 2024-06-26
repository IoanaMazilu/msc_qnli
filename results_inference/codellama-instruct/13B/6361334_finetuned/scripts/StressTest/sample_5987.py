boxes_sold_mark_premise = n - 6
boxes_sold_ann_premise = n - 2
boxes_sold_mark_hypothesis = n - 6
boxes_sold_ann_hypothesis = n - 2

# the hypothesis refers to the number of boxes sold by Mark and Ann, which are also mentioned in the premise
if boxes_sold_mark_hypothesis!= boxes_sold_mark_premise:
    # check if the number of boxes sold by Mark in the hypothesis contradicts the number of boxes sold by Mark in the premise
    label = "contradiction"
elif boxes_sold_ann_hypothesis!= boxes_sold_ann_premise:
    # check if the number of boxes sold by Ann in the hypothesis contradicts the number of boxes sold by Ann in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
