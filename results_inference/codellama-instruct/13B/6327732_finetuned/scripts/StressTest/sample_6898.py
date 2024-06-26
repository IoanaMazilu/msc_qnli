boxes_sold_mark_premise = 6
boxes_sold_ann_premise = 2
boxes_sold_mark_hypothesis = 7
boxes_sold_ann_hypothesis = 2

# the hypothesis refers to the number of boxes sold by Mark and Ann, mentioned in the premise
if boxes_sold_mark_hypothesis <= boxes_sold_mark_premise:
    # check if the estimate of 'boxes_sold_mark_hypothesis' contradicts the number of boxes sold by Mark in the premise
    label = "contradiction"
elif boxes_sold_ann_hypothesis!= boxes_sold_ann_premise:
    # check if the number of boxes sold by Ann in the hypothesis contradicts the number of boxes sold by Ann reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
