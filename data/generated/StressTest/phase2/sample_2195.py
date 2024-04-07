# Premise: During the first two weeks of June, the total rainfall in Springdale was 40 inches.
# Hypothesis: During the first two weeks of June, the total rainfall in Springdale was 70 inches.
# Golden Label: contradiction

rainfall_premise = 40
rainfall_hypothesis = 70

# the hypothesis refers to the amount of rainfall in June, mentioned also in the premise
if rainfall_hypothesis != rainfall_premise:
    # check if the amount of rainfall in the hypothesis contradicts the amount of rainfall reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

