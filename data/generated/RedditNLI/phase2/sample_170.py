# Premise: Unprecedented Inequality: The Top 1 Percent Captured 95% of the Income Gains Since 2009.
# Hypothesis: 95% of 2009-2012 Income Gains Went to the Top 1%.
# Golden Label: entailment

percentage_income_gain_premise = 95
percentage_income_gain_hypothesis = 95

# the hypothesis and premise mention the percentage of income gains captured by the top 1 percent
if percentage_income_gain_hypothesis != percentage_income_gain_premise:
    # check if the percentage of income gains in the hypothesis contradicts the percentage of income gains in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

