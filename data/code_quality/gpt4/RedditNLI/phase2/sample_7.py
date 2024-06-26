income_premise = 600e6
income_hypothesis = 500e6

# the hypothesis and premise mention Schwartzman's income
if income_hypothesis > income_premise:
    # check if the income mentioned in the hypothesis contradicts the income mentioned in the premise
    label = "contradiction"
elif income_hypothesis < income_premise:
    # the premise gives only an estimate for the income
    # any estimate of the income in the hypothesis lower than 'income_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
