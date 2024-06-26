years_future_premise = 25
years_future_hypothesis = 15
years_past = 15
quadrice = 4

# The hypothesis and premise both talk about Karthik's age in terms of how many times his age years ago
# The time frames differ, one is less than 25 years hence and the other is 15 years hence

if years_future_hypothesis >= years_future_premise:
    # check if the time frame in the hypothesis contradicts the premise's time frame
    label = "contradiction"
else:
    # the premise gives an upper limit for the time frame
    # any time frame less than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
