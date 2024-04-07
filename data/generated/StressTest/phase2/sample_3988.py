# Premise: less than 25 years hence, Karthik will be just Quadrice as old as he was 15 years ago, How old is Karthik at now? [ Quadrice = 4 Times ].
# Hypothesis: 15 years hence, Karthik will be just Quadrice as old as he was 15 years ago, How old is Karthik at now? [ Quadrice = 4 Times ].
# Golden Label: neutral

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

