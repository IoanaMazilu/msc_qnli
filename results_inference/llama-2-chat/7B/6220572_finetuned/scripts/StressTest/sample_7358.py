total_age_premise = 45
total_age_hypothesis = 75

if total_age_hypothesis < total_age_premise:
    # check if the total age in the hypothesis contradicts the total age in the premise
    label = "contradiction"
else:
    # any total age greater than 'total_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
