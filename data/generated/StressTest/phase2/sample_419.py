# Premise: If Jerry wants to raise his average by 2 points, what score must he earn on the fourth test?
# Hypothesis: If Jerry wants to raise his average by 3 points, what score must he earn on the fourth test?
# Golden Label: contradiction

average_increase_premise = 2
average_increase_hypothesis = 3

# the hypothesis refers to the increase in average Jerry wants to achieve, which is also mentioned in the premise
if average_increase_premise != average_increase_hypothesis:
    # check if the desired increase in average in the hypothesis contradicts the desired increase in the premise
    label = "contradiction"
else:
    # if the desired increase in average in the hypothesis matches the one in the premise, we can infer entailment
    label = "entailment"

print(label)

