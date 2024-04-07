# Premise: If each runner is to race onto their assigned line (and not in the middle of the lane), and Tom is to run on line 1 and Bob on line 8.
# Hypothesis: If each runner is to race onto their assigned line (and not in the middle of the lane), and Tom is to run on line 8 and Bob on line 8.
# Golden Label: contradiction

tom_line_premise = 1
bob_line_premise = 8
tom_line_hypothesis = 8
bob_line_hypothesis = 8

# the hypothesis refers to the running lines of Tom and Bob mentioned in the premise
if tom_line_hypothesis != tom_line_premise:
    # check if the running line of Tom in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif bob_line_hypothesis != bob_line_premise:
    # check if the running line of Bob in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

