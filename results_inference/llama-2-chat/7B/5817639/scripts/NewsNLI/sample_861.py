sharon_age_premise = 85
sharon_age_hypothesis = 85

# the hypothesis mentions the age of Ariel Sharon, which is also referenced in the premise
if sharon_age_hypothesis == sharon_age_premise:
    # if the hypothesis value matches the premise value, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value contradicts the premise value, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer neutrality
    label = "neutral"

print(label)
