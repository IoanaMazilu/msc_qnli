# Premise: Karen sold 36.0 boxes of Tagalongs.
# Hypothesis: Karen picked up 6.0 cases of 12.0 boxes.
# Golden Label: contradiction

boxes_sold_premise = 36.0
cases_hypothesis = 6.0
boxes_per_case_hypothesis = 12.0

# the hypothesis refers to the number of boxes, which is also mentioned in the premise
# compute the total number of boxes in the hypothesis
total_boxes_hypothesis = cases_hypothesis * boxes_per_case_hypothesis
if total_boxes_hypothesis != boxes_sold_premise:
    # check if the number of boxes in the hypothesis contradicts the number of boxes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

