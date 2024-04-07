# Premise: The total of the ages of Amar, Akbar and Anthony is more than 16 years.
# Hypothesis: The total of the ages of Amar, Akbar and Anthony is 36 years.
# Golden Label: neutral

total_age_premise = 16
total_age_hypothesis = 36

# the hypothesis talks about the total age of Amar, Akbar and Anthony, referenced also in the premise
if total_age_hypothesis <= total_age_premise:
    # check if the hypothesis value contradicts the estimate of more than 'total_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total age
    # any total age greater than 'total_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

