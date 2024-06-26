boxes_sold_premise = 12.0
cases_needed_hypothesis = 1.0
extra_boxes_hypothesis = 12.0

# the hypothesis refers to the number of boxes needed, which are also mentioned in the premise
# compute the total number of boxes needed from the hypothesis
total_boxes_needed = cases_needed_hypothesis * 12.0
if total_boxes_needed > boxes_sold_premise:
    # check if the number of boxes needed from the hypothesis contradicts the number of boxes sold in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
