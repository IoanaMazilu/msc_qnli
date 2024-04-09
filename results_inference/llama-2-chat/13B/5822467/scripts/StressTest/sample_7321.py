gym_frequency_premise = 2 * 6 / 7  # 2 times per week on average for the past less than 6 weeks
gym_frequency_hypothesis = 2 * 3 / 7  # 2 times per week on average for the past 3 weeks

# check if the hypothesis value contradicts the estimate of the premise
if gym_frequency_hypothesis <= gym_frequency_premise:
    label = "contradiction"
elif gym_frequency_hypothesis > gym_frequency_premise:
    # the hypothesis value is greater than the estimate of the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the gym frequency
    # any frequency that is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
