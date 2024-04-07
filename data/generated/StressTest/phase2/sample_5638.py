# Premise: Suresh age after less than 85 years will be 5 times his age 5 years back, What is the present age of Suresh.
# Hypothesis: Suresh age after 15 years will be 5 times his age 5 years back, What is the present age of Suresh.
# Golden Label: neutral

years_future_premise = 85
years_future_hypothesis = 15

# the hypothesis talks about the future age of Suresh, referenced also in the premise
if years_future_hypothesis >= years_future_premise:
    # check if the hypothesis value contradicts the estimate of less than 'years_future_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the future age of Suresh
    # any number of years less than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

