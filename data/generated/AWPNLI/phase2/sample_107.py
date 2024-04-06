# Premise: Jenny sold 24.0 boxes of Trefoils.
# Hypothesis: Jenny needed 1.0 cases of 8.0 boxes, plus extra boxes.
# Golden Label: contradiction

sold_boxes_premise = 24.0
cases_needed_hypothesis = 1.0
boxes_per_case_hypothesis = 8.0

# the hypothesis refers to the number of boxes, which are also mentioned in the premise
# compute the total number of boxes in the hypothesis
total_boxes_hypothesis = cases_needed_hypothesis * boxes_per_case_hypothesis

if total_boxes_hypothesis > sold_boxes_premise:
    # check if the number of boxes in the hypothesis contradicts the number of boxes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

