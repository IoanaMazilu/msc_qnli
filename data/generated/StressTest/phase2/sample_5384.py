# Premise: During the first two weeks of February, the total rainfall in Springdale was 20 inches.
# Hypothesis: During the first two weeks of February, the total rainfall in Springdale was less than 20 inches.
# Golden Label: contradiction

rainfall_premise = 20
rainfall_hypothesis = 20

# the hypothesis refers to the amount of rainfall in the first two weeks of February, which is also mentioned in the premise
if rainfall_hypothesis >= rainfall_premise:
    # check if the hypothesis value contradicts the premise's statement of 'less than rainfall_premise' inches of rain
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

