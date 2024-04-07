# Premise: The total of the ages of Amar, Akbar and Anthony is 80 years.
# Hypothesis: The total of the ages of Amar, Akbar and Anthony is less than 80 years.
# Golden Label: contradiction

total_age_premise = 80
total_age_hypothesis = 80

# the hypothesis states about the total age of Amar, Akbar and Anthony, which is also mentioned in the premise
if total_age_hypothesis >= total_age_premise:
    # check if the hypothesis value contradicts the exact total age mentioned in the premise
    label = "contradiction"
elif total_age_hypothesis == total_age_premise:
    # check if the total age in the hypothesis matches exactly with the total age mentioned in the premise
    label = "entailment"
else:
    # the premise gives the exact total age
    # any total age less than 'total_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

