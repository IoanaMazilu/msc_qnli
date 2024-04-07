# Premise: 20,000 for less than 7 months, where as Rick invested his amount for the whole year, what was the amount invested by Rick?
# Hypothesis: 20,000 for 6 months, where as Rick invested his amount for the whole year, what was the amount invested by Rick?
# Golden Label: neutral

investment_duration_premise = 7
investment_duration_hypothesis = 6

# the hypothesis refers to the duration of investment which is also mentioned in the premise
if investment_duration_hypothesis >= investment_duration_premise:
    # check if the investment duration in the hypothesis contradicts the premise's statement of 'less than 7 months'
    label = "contradiction"
elif investment_duration_hypothesis < investment_duration_premise:
    # the hypothesis duration of '6 months' does not contradict 'less than 7 months' from the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)

