sandy_age_premise = 4
molly_age_premise = 3

# define variables for the hypothesized ratio
sandy_age_hypothesis = 5
molly_age_hypothesis = 4

# check if the hypothesis ratio is more than the premise ratio
if sandy_age_hypothesis / molly_age_hypothesis > sandy_age_premise / molly_age_premise:
    # the hypothesis ratio is greater than the premise ratio, so we have entailment
    label = "entailment"
elif sandy_age_hypothesis / molly_age_hypothesis <= sandy_age_premise / molly_age_premise:
    # the hypothesis ratio is less than or equal to the premise ratio, so we have contradiction
    label = "contradiction"
else:
    # the hypothesis ratio is neutral with respect to the premise ratio
    label = "neutral"

print(label)
