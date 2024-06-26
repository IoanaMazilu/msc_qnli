sold_boxes_premise = 20.0
needed_cases_hypothesis = 5.0
boxes_per_case_hypothesis = 4.0

# compute the total number of boxes in the hypothesis
total_boxes_hypothesis = needed_cases_hypothesis * boxes_per_case_hypothesis

# since we don't know how many extra boxes are there, there is no way to compare the total boxes in the hypothesis and premise
# so we cannot infer entailment or contradiction
label = "neutral"

print(label)
