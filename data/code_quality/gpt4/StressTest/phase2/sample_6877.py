total_age_premise = 86
total_age_hypothesis = 66

# the hypothesis refers to the total age of Amar, Akbar and Anthony referenced in the premise
if total_age_hypothesis >= total_age_premise:
    # check if the total age in the hypothesis contradicts the premise's estimate of less than 'total_age_premise'
    label = "contradiction"
elif total_age_hypothesis < total_age_premise:
    # if the total age in the hypothesis is less than 'total_age_premise', the hypothesis can be fully entailed from the premise
    label = "entailment"

print(label)
