# Premise: Suresh age after 15 years will be 5 times his age 5 years back, What is the present age of Suresh.
# Hypothesis: Suresh age after less than 15 years will be 5 times his age 5 years back, What is the present age of Suresh.
# Golden Label: contradiction

years_future_premise = 15
years_future_hypothesis = 15
years_past = 5

# the hypothesis talks about a future age of Suresh, referenced also in the premise
if years_future_hypothesis < years_future_premise:
    # check if the hypothesis value contradicts the premise value of 'years_future_premise'
    label = "contradiction"
else:
    # the premise gives the exact number of years for Suresh's age in the future
    # any number of years equal or more than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

