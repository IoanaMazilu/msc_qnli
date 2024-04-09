# define variables for numerical entities in the premise and hypothesis
hours_premise = 35
rate_premise = 1.0
additional_hours_premise = 0
hours_hypothesis = float(input("Enter the number of hours worked per week: "))
rate_hypothesis = 1.5

# extract numerical values from the premise and hypothesis
rate_premise = float(rate_premise)
additional_hours_premise = float(additional_hours_premise)

# compare the values to determine the label
if hours_hypothesis > hours_premise:
    # the hypothesis implies more hours worked than in the premise, so contradiction
    label = "contradiction"
elif hours_hypothesis == hours_premise:
    # the hypothesis and premise are equal, so neutral
    label = "neutral"
else:
    # the hypothesis implies fewer hours worked than in the premise, so entailment
    label = "entailment"

print(label)
