# Premise: Molly's age in 18 years will be six times her age seven years ago.
# Hypothesis: Molly's age in less than 88 years will be six times her age seven years ago.
# Golden Label: entailment

# define the variables
future_age_multiplier = 6
past_age_years_ago = 7
future_age_years_premise = 18
future_age_years_hypothesis = 88

# the hypothesis refers to Molly's age in future years, which is also mentioned in the premise
if future_age_years_hypothesis < future_age_years_premise:
    # check if the 'future_age_years_hypothesis' contradicts the 'future_age_years_premise'
    label = "contradiction"
else:
    # if the 'future_age_years_hypothesis' does not contradict the 'future_age_years_premise', it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

