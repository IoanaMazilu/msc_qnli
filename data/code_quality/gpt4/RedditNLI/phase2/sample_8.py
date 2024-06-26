annual_income_premise = 700
annual_income_hypothesis = 600

# the hypothesis and premise mention the annual income of Steven Schwartzman
if annual_income_hypothesis > annual_income_premise:
    # check if the annual income in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the annual income in the hypothesis is less or equal to the amount in the premise, it is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
