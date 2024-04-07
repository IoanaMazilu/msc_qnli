# Premise: Shawn invested one half of his savings in a bond that paid simple interest for 2 years and received $400 as interest.
# Hypothesis: Shawn invested one half of his savings in a bond that paid simple interest for less than 2 years and received $400 as interest.
# Golden Label: contradiction

interest_premise = 400
interest_hypothesis = 400
investment_time_premise = 2
investment_time_hypothesis = 2

# the hypothesis talks about the amount of interest and the time of investment, both mentioned in the premise
if interest_hypothesis != interest_premise:
    # check if the amount of interest in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
elif investment_time_hypothesis >= investment_time_premise:
    # check if the time of investment in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # the hypothesis value and time do not contradict the premise ones, but the time cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

