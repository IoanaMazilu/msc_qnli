income_premise = 500
income_hypothesis = 600

# the hypothesis and premise mention the annual income of Mr Schwartzfman
if income_hypothesis < income_premise:
    # check if the income in the hypothesis contradicts the premise of more than 'income_premise' dollars
    label = "contradiction"
else:
    # the premise gives only a minimum for the income
    # any income in the hypothesis greater or equal to 'income_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
