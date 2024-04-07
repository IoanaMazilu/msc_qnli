# Premise: The total of the ages of Amar, Akbar and Anthony is less than 70 years.
# Hypothesis: The total of the ages of Amar, Akbar and Anthony is 40 years.
# Golden Label: neutral

total_age_premise = 70
total_age_hypothesis = 40

# the hypothesis refers to the total age of Amar, Akbar and Anthony, also mentioned in the premise
if total_age_hypothesis >= total_age_premise:
    # check if the total age in the hypothesis contradicts the estimate of less than 'total_age_premise'
    label = "contradiction"
else:
    # if the total age in the hypothesis does not contradict the estimate in the premise
    # but we cannot fully entail it from the premise because the premise only gives an upper limit
    label = "neutral"

print(label)

