sold_boxes_premise = 20.0
needed_cases_hypothesis = 3.0
boxes_per_case_hypothesis = 4.0

# the hypothesis refers to the number of boxes, which are also mentioned in the premise
# compute the total number of boxes in the hypothesis
total_boxes_hypothesis = needed_cases_hypothesis * boxes_per_case_hypothesis

if total_boxes_hypothesis > sold_boxes_premise:
    # check if the total boxes in the hypothesis contradicts the number of sold boxes in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
