# Premise: The son lived just 1/2 of what Adam lived.
# Hypothesis: The son lived just less than 5/2 of what Adam lived.
# Golden Label: entailment

son_life_premise = 1/2
son_life_hypothesis = 5/2

# the hypothesis refers to the ratio of son's life to Adam's life, which is also mentioned in the premise
if son_life_hypothesis == son_life_premise:
    # check if the ratio in the hypothesis matches the ratio in the premise
    label = "entailment"
elif son_life_hypothesis < son_life_premise:
    # check if the ratio in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # the hypothesis value is more than the premise one
    # the premise does not provide enough information to fully entail the hypothesis
    label = "neutral"

print(label)

