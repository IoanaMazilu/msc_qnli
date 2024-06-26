future_age_premise = 38
future_age_hypothesis = 18
past_age = 6

# The hypothesis talks about Molly's age in a certain number of years, 
# same as the premise, but the number of years is different
if future_age_hypothesis >= future_age_premise:
    # check if the number of years in the future mentioned in the hypothesis contradicts the estimate of less than 'future_age_premise' years
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years in the future
    # any number of years less than 'future_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
