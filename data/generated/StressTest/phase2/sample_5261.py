# Premise: During the first two weeks of May, the total rainfall in Springdale was 35 inches.
# Hypothesis: During the first two weeks of May, the total rainfall in Springdale was 25 inches.
# Golden Label: contradiction

rainfall_premise = 35
rainfall_hypothesis = 25

# the hypothesis refers to the total rainfall in first two weeks of May mentioned in the premise
if rainfall_premise != rainfall_hypothesis:
    # check if the total rainfall in the hypothesis contradicts the total rainfall mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

