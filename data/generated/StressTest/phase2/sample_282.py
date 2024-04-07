# Premise: What will be Sona's age after 6 years?
# Hypothesis: What will be Sona's age after more than 1 years?
# Golden Label: entailment

sona_age_years_premise = 6
sona_age_years_hypothesis = 1

# the hypothesis refers to the number of years after which we want to know Sona's age, mentioned in the premise
if sona_age_years_premise <= sona_age_years_hypothesis:
    # check if the estimate of 'sona_age_years_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'sona_age_years_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

