total_age_premise = 45
total_age_hypothesis = 75

# the hypothesis talks about the total age of 3 people, referenced also in the premise
if total_age_hypothesis > total_age_premise:
    # check if the hypothesis value contradicts the estimate of 'total_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total age
    # any total age greater than 'total_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
