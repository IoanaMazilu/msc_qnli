# Premise: Kishore saved less than 80% of his monthly salary.
# Hypothesis: Kishore saved 10% of his monthly salary.
# Golden Label: neutral

salary_savings_premise = 80
salary_savings_hypothesis = 10

# the hypothesis talks about the percentage of the salary that Kishore saved, which is also mentioned in the premise
if salary_savings_hypothesis >= salary_savings_premise:
    # check if the hypothesis value contradicts the estimate of less than 'salary_savings_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the savings
    # any percentage of savings less than 'salary_savings_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

