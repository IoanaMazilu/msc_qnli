# Premise: If each runner is to race onto their assigned line (and not in the middle of the lane), and Tom is to run on line less than 8 and Bob on line 8.
# Hypothesis: If each runner is to race onto their assigned line (and not in the middle of the lane), and Tom is to run on line 1 and Bob on line 8.
# Golden Label: neutral

tom_line_premise = 8
bob_line_premise = 8
tom_line_hypothesis = 1
bob_line_hypothesis = 8

# the hypothesis refers to the lines on which Tom and Bob are supposed to run, as mentioned in the premise
if tom_line_hypothesis >= tom_line_premise:
    # check if the line assigned to Tom in the hypothesis contradicts the premise
    label = "contradiction"
elif bob_line_hypothesis != bob_line_premise:
    # check if the line assigned to Bob in the hypothesis contradicts the one mentioned in the premise
    label = "contradiction"
else:
    # if the lines assigned to Tom and Bob in the hypothesis do not contradict the ones mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)

