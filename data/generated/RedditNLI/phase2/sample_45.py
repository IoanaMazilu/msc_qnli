# Premise: 95% of 2009-2012 Income Gains Went to the Top 1%.
# Hypothesis: Unprecedented Inequality: The Top 1 Percent Captured 95% of the Income Gains Since 2009.
# Golden Label: entailment

percentage_income_gains_premise = 95
percentage_income_gains_hypothesis = 95

# the hypothesis and premise mention the percentage of income gains captured by the top 1%
if percentage_income_gains_premise != percentage_income_gains_hypothesis:
    # check if the percentage of income gains in the hypothesis contradicts the percentage of income gains in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

