# Premise: Dan's age after more than 10 years will be 7 times his age 4 years ago.
# Hypothesis: Dan's age after 20 years will be 7 times his age 4 years ago.
# Golden Label: neutral

years_future_premise = 10
years_future_hypothesis = 20
time_past = 4
age_factor = 7

# the hypothesis talks about Dan's future and past age, referenced also in the premise
if years_future_hypothesis <= years_future_premise:
    # check if the hypothesis value contradicts the estimate of more than 'years_future_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the years in the future
    # any number of years greater than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

