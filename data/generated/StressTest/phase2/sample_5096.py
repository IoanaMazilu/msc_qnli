# Premise: If Jerry wants to raise his average by 3 points, what score must he earn on the fourth test?
# Hypothesis: If Jerry wants to raise his average by more than 3 points, what score must he earn on the fourth test?
# Golden Label: contradiction

average_raise_premise = 3
average_raise_hypothesis = 3

# the hypothesis refers to the average raise mentioned in the premise
if average_raise_premise < average_raise_hypothesis:
    # check if the desired average raise in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

