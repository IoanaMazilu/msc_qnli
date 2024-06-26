cost_per_day_premise = 0.5
cost_per_day_hypothesis = 0.5
frequency_premise = 42
frequency_hypothesis = 12

# the hypothesis refers to the cost and frequency of charges for internet traffic mentioned in the premise
if cost_per_day_hypothesis != cost_per_day_premise:
    # check if the cost per day in the hypothesis contradicts the cost per day reported in the premise
    label = "contradiction"
elif frequency_hypothesis >= frequency_premise:
    # check if the frequency of charges in the hypothesis contradicts the estimate of less than 'frequency_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the frequency of charges
    # any frequency less than 'frequency_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
