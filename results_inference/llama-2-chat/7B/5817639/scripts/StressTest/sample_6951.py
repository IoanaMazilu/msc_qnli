age_premise = 5
age_hypothesis = 2

# the hypothesis talks about Arun's age being more than 2 years, referenced in the premise
if age_hypothesis <= age_premise:
    # check if the hypothesis value contradicts the estimate of Arun's age in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for Arun's age, and any age greater than that estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
