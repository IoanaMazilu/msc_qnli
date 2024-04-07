# Premise: Aamir saves less than 82% of his monthly salary.
# Hypothesis: Aamir saves 32% of his monthly salary.
# Golden Label: neutral

salary_savings_premise = 82
salary_savings_hypothesis = 32

# the hypothesis refers to the percentage of salary Aamir saves, mentioned also in the premise
if salary_savings_hypothesis >= salary_savings_premise:
    # check if the percentage of 'salary_savings_hypothesis' contradicts the estimate of less than 'salary_savings_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of salary savings
    # any percentage of salary savings less than 'salary_savings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

