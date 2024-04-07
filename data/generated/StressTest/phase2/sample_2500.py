# Premise: Aamir saves less than 52% of his monthly salary.
# Hypothesis: Aamir saves 32% of his monthly salary.
# Golden Label: neutral

salary_savings_premise = 52
salary_savings_hypothesis = 32

# the hypothesis talks about the percentage of Aamir's salary savings, referenced also in the premise
if salary_savings_hypothesis >= salary_savings_premise:
    # check if the hypothesis value contradicts the estimate of less than 'salary_savings_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of salary saved
    # any percentage of savings less than 'salary_savings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

