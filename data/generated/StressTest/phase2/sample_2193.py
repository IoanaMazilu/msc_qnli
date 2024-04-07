# Premise: During the first two weeks of June, the total rainfall in Springdale was 40 inches.
# Hypothesis: During the first two weeks of June, the total rainfall in Springdale was more than 20 inches.
# Golden Label: entailment

rainfall_premise = 40
rainfall_hypothesis = 20

# the hypothesis is referring to the total rainfall in June, as mentioned in the premise
if rainfall_hypothesis >= rainfall_premise:
    # check if the hypothesis estimate contradicts the premise value of 'rainfall_premise'
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

