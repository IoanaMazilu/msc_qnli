# Premise: The total of the ages of Amar, Akbar and Anthony is 36 years.
# Hypothesis: The total of the ages of Amar, Akbar and Anthony is more than 16 years.
# Golden Label: entailment

total_age_premise = 36
total_age_hypothesis = 16

# The hypothesis refers to the total age of Amar, Akbar and Anthony mentioned in the premise
if total_age_premise < total_age_hypothesis:
    # Check if the total age in the premise contradicts the minimum total age in the hypothesis
    label = "contradiction"
elif total_age_premise == total_age_hypothesis:
    # If the total ages in the premise and hypothesis are the same, it implies entailment
    label = "entailment"
else:
    # Any total age greater than 'total_age_hypothesis' is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)

