earnings_increase_percentage_premise = 36
earnings_after_increase_premise = 495

earnings_increase_percentage_hypothesis = 36
earnings_after_increase_hypothesis = 495

# The hypothesis refers to the increase in Albert's monthly earnings and the final earnings figure
# mentioned in the premise

if earnings_after_increase_hypothesis != earnings_after_increase_premise:
    # Check if the final earnings figure in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
elif earnings_increase_percentage_hypothesis <= earnings_increase_percentage_premise:
    # Check if the increase percentage in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # The premise gives an exact percentage for the increase in earnings
    # Any percentage higher than 'earnings_increase_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
