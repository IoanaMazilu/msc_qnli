# Premise: What will be Sona's age after more than 1 years?
# Hypothesis: What will be Sona's age after 6 years?
# Golden Label: neutral

sona_age_after_years_premise = 1
sona_age_after_years_hypothesis = 6

# the hypothesis talks about Sona's age after a number of years, referenced also in the premise
if sona_age_after_years_hypothesis <= sona_age_after_years_premise:
    # check if the hypothesis value contradicts the estimate of more than 'sona_age_after_years_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'sona_age_after_years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

