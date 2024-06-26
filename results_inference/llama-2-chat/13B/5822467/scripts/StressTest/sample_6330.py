cases_premise = 5
boxes_per_case_premise = 1
hours_premise = 2

# define variables for the hypotheses
cases_hypothesis = 8
boxes_per_case_hypothesis = 1

# calculate the total number of boxes in the hypothesis
total_boxes_hypothesis = cases_hypothesis * boxes_per_case_hypothesis

# calculate the total number of boxes in the premise
total_boxes_premise = cases_premise * boxes_per_case_premise

# check if the hypothesis is consistent with the premise
if total_boxes_hypothesis <= total_boxes_premise:
    label = "entailment"
elif total_boxes_hypothesis > total_boxes_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
