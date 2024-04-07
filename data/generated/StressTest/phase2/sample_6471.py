# Premise: 4000 but the average salary of Raj, Roshan and Thomas is Rs.
# Hypothesis: less than 5000 but the average salary of Raj, Roshan and Thomas is Rs.
# Golden Label: entailment

avg_salary_premise = 4000
avg_salary_hypothesis = 5000

# the hypothesis refers to the average salary of Raj, Roshan and Thomas mentioned in the premise
if avg_salary_hypothesis <= avg_salary_premise:
    # check if the estimate of 'avg_salary_hypothesis' contradicts the average salary in the premise
    label = "contradiction"
else:
    # the premise gives only an exact value for the average salary
    # any value of average salary greater than 'avg_salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

