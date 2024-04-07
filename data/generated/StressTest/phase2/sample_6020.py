# Premise: Jane is currently 32 years old, and she stopped baby-sitting 10 years ago.
# Hypothesis: Jane is currently more than 32 years old, and she stopped baby-sitting 10 years ago.
# Golden Label: contradiction

jane_age_premise = 32
jane_age_hypothesis = 32
years_since_babysitting_premise = 10
years_since_babysitting_hypothesis = 10

# The hypothesis refers to Jane's age and the number of years since she stopped babysitting, both mentioned in the premise
if jane_age_hypothesis != jane_age_premise:
    # Check if the hypothesis value contradicts the premise's statement about Jane's age
    label = "contradiction"
elif years_since_babysitting_hypothesis != years_since_babysitting_premise:
    # Check if the hypothesis value contradicts the premise's statement about the number of years since Jane stopped babysitting
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the ones from the premise, we can infer entailment
    label = "entailment"

print(label)

