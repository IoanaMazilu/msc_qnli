# Premise: Kishore saved less than 20% of his monthly salary.
# Hypothesis: Kishore saved 10% of his monthly salary.
# Golden Label: neutral

salary_saved_premise = 20
salary_saved_hypothesis = 10

# the hypothesis refers to the percentage of salary saved by Kishore, also mentioned in the premise
if salary_saved_hypothesis >= salary_saved_premise:
    # check if the hypothesis value contradicts the estimate of less than 'salary_saved_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage saved
    # any percentage less than 'salary_saved_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

