# Define variables
future_age_premise = 38
future_age_hypothesis = 18
past_age = 18

# The hypothesis talks about Molly's age in the future and the past, which is also mentioned in the premise
if future_age_hypothesis >= future_age_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise provides an upper limit for Molly's future age
    # any number less than 'future_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
