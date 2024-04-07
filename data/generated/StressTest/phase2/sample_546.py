# Premise: If each runner is to race onto their assigned line (and not in the middle of the lane), and Tom is to run on line 1 and Bob on line 8.
# Hypothesis: If each runner is to race onto their assigned line (and not in the middle of the lane), and Tom is to run on line less than 8 and Bob on line 8.
# Golden Label: entailment

line_tom_premise = 1
line_tom_hypothesis = 8
line_bob_premise = 8
line_bob_hypothesis = 8

# the hypothesis refers to the lines assigned to Tom and Bob, also mentioned in the premise
if line_tom_hypothesis <= line_tom_premise:
    # check if the line assigned to Tom in the hypothesis contradicts the line assigned to him in the premise
    label = "contradiction"
elif line_bob_hypothesis != line_bob_premise:
    # check if the line assigned to Bob in the hypothesis contradicts the line assigned to him in the premise
    label = "contradiction"
else:
    # if the lines in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)

