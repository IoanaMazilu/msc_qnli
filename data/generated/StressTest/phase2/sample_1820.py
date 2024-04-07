# Premise: Dan's age after 20 years will be 7 times his age 4 years ago.
# Hypothesis: Dan's age after less than 20 years will be 7 times his age 4 years ago.
# Golden Label: contradiction

years_in_future_premise = 20
years_in_future_hypothesis = 20
multiplier_age_past = 7
years_in_past = 4

# the hypothesis and premise refer to Dan's age in future and past years
if years_in_future_hypothesis >= years_in_future_premise:
    # check if the hypothesis contradicts the premise about the number of years in future
    label = "contradiction"
else:
    # the premise gives a certain number of years in future, 
    # any number of years less than 'years_in_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

