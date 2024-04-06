# Premise: US retail sales fall 0.4 percent in March, most in 9 months.
# Hypothesis: Retail sales post biggest drop in 9 months.
# Golden Label: entailment

drop_percent_premise = 0.4
months_premise = 9

# The hypothesis asserts that the drop in sales was the biggest in the same period of 9 months, without providing a value for the drop.
# Without a numerical value in the hypothesis for the drop, we can't compare it with the drop in the premise.
# Since the drop in the premise is the biggest in 9 months, the hypothesis is consistent with the premise, but it cannot be explicitly entailed from the premise.
label = "neutral"

print(label)

