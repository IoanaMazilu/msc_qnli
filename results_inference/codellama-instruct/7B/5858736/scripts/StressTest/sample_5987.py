boxes_sold_premise = 6
boxes_sold_hypothesis = 6

# the hypothesis refers to the number of boxes sold by Mark and Ann
if boxes_sold_hypothesis <= boxes_sold_premise:
    # check if the estimate of 'boxes_sold_hypothesis' contradicts the number of boxes sold by Mark
    label = "contradiction"
elif boxes_sold_hypothesis!= boxes_sold_premise:
    # check if the number of boxes sold by Ann in the hypothesis contradicts the number of boxes sold by Ann reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
