boxes_sold_premise = 12.0
cases_needed_hypothesis = 1.0
extra_boxes_hypothesis = 12.0

# the hypothesis refers to the number of boxes sold and the number of cases needed, which are also mentioned in the premise
# compute the total number of boxes sold
total_boxes_premise = boxes_sold_premise
if total_boxes_premise!= cases_needed_hypothesis * 12.0 + extra_boxes_hypothesis:
    # check if the number of boxes in the hypothesis contradicts the number of boxes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
