# Premise: The largest protest was in Taiz, where more than 500,000 went into Freedom Square, numerous eyewitnesses estimated.
# Hypothesis: Witnesses say more than 500,000 protesters gather in Taiz.
# Golden Label: entailment

protesters_premise = 500000
protesters_hypothesis = 500000

# the hypothesis mentions the number of protesters in Taiz, which is also referenced in the premise
if protesters_hypothesis != protesters_premise:
    # check if the number of protesters in the hypothesis contradicts the number of protesters reported in the premise
    label = "contradiction"
else:
    # if the number of protesters in the hypothesis does not contradict the number of protesters in the premise, we can infer entailment
    label = "entailment"

print(label)
