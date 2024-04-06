# Premise: Ashley sold 12.0 boxes of Samoas.
# Hypothesis: Ashley needed 1.0 cases of 12.0 boxes, plus extra boxes.
# Golden Label: entailment

sold_boxes_premise = 12.0
needed_cases_hypothesis = 1.0
boxes_per_case_hypothesis = 12.0

# the hypothesis refers to the number of boxes which is also mentioned in the premise
# compute the number of boxes needed in the hypothesis
needed_boxes_hypothesis = needed_cases_hypothesis * boxes_per_case_hypothesis
if sold_boxes_premise != needed_boxes_hypothesis:
    # check if the number of boxes in the hypothesis contradicts the number of boxes from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

