father_age_premise = 10 + 2 * Shankar_age
father_age_hypothesis = 2 * Shankar_age < 80

# Check if the hypothesis value contradicts the estimate of father's age in the premise
if father_age_hypothesis > father_age_premise:
    label = "contradiction"
elif father_age_hypothesis == father_age_premise:
    # If the hypothesis value is equal to the estimate, there is no contradiction or entailment
    label = "neutral"
else:
    # If the hypothesis value is less than the estimate, we can infer entailment
    label = "entailment"

print(label)
