# Premise: If Jerry wants to raise his average by 2 points, what score must he earn on the fourth test?
# Hypothesis: If Jerry wants to raise his average by less than 8 points, what score must he earn on the fourth test?
# Golden Label: entailment

raise_avg_premise = 2
raise_avg_hypothesis = 8

# the hypothesis refers to Jerry's need to raise his average, also mentioned in the premise
if raise_avg_hypothesis < raise_avg_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif raise_avg_hypothesis > raise_avg_premise:
    # if the hypothesis value is greater than the premise one, we cannot infer entailment
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

