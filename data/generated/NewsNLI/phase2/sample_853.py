# Premise: Only 14 percent of Americans say an impending terrorist attack is likely in their community.
# Hypothesis: 30 percent said they think an attack on American soil is likely soon.
# Golden Label: neutral

likelihood_premise = 0.14
likelihood_hypothesis = 0.30

# the hypothesis mentions the likelihood of an attack on American soil, which is also mentioned in the premise
if likelihood_hypothesis > likelihood_premise:
    # check if the likelihood in the hypothesis contradicts the likelihood reported in the premise
    label = "contradiction"
else:
    # if the likelihood in the hypothesis does not contradict the likelihood in the premise, we can infer entailment
    label = "neutral"

print(label)

