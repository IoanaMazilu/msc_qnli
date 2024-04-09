total_age_premise = 86
total_age_hypothesis = 66

# the hypothesis refers to the total age of Amar, Akbar and Anthony mentioned in the premise
if total_age_hypothesis >= total_age_premise:
    # check if the total age in the hypothesis contradicts the premise of less than 'total_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total age
    # any total age less than 'total_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
