# Premise: The total of the ages of Amar, Akbar and Anthony is 40 years.
# Hypothesis: The total of the ages of Amar, Akbar and Anthony is less than 70 years.
# Golden Label: entailment

total_age_premise = 40
total_age_hypothesis = 70

# the hypothesis refers to the total age of Amar, Akbar and Anthony mentioned in the premise
if total_age_hypothesis < total_age_premise:
    # check if the total age in the hypothesis contradicts the total age mentioned in the premise
    label = "contradiction"
elif total_age_hypothesis == total_age_premise:
    # check if the total age in the hypothesis can be fully and explicitly entailed from the premise
    label = "entailment"
else:
    # any total age greater than 'total_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

