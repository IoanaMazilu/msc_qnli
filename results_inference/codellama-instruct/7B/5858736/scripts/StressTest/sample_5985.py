boxes_sold_premise_mark = 6
boxes_sold_premise_ann = 2
boxes_sold_hypothesis_mark = 1
boxes_sold_hypothesis_ann = 2

# the hypothesis refers to the number of boxes sold by Mark and Ann
if boxes_sold_hypothesis_mark <= boxes_sold_premise_mark:
    # check if the estimate of 'boxes_sold_hypothesis_mark' contradicts the number of boxes sold by Mark in the premise
    label = "contradiction"
elif boxes_sold_hypothesis_ann!= boxes_sold_premise_ann:
    # check if the number of boxes sold by Ann in the hypothesis contradicts the number of boxes sold by Ann reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
