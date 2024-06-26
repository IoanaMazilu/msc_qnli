income_increase_premise = 50
income_increase_hypothesis = 40

# the hypothesis refers to the percentage of income increase which is also mentioned in the premise
if income_increase_hypothesis >= income_increase_premise:
    # check if the hypothesis value contradicts the premise value of 'income_increase_premise'
    label = "contradiction"
elif income_increase_hypothesis < income_increase_premise:
    # the premise gives an estimate for the income increase
    # any increase less than 'income_increase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
