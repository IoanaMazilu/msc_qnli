# Premise: Mary has a monthly salary of $less than 3200.
# Hypothesis: Mary has a monthly salary of $1200.
# Golden Label: neutral

salary_premise = 3200
salary_hypothesis = 1200

# the hypothesis refers to the salary of Mary mentioned in the premise
if salary_hypothesis >= salary_premise:
    # check if the value of 'salary_hypothesis' contradicts the estimate of less than 'salary_premise'
    label = "contradiction"
elif salary_hypothesis < salary_premise:
    # the premise gives only an estimate for the salary
    # any salary less than 'salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

