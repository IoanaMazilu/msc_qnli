average_salary_premise = 4000
average_salary_hypothesis = 5000

# the hypothesis refers to the average salary of Raj, Roshan, and Thomas
if average_salary_hypothesis <= average_salary_premise:
    # check if the hypothesis value contradicts the estimate of the average salary in the premise
    label = "contradiction"
elif average_salary_hypothesis > average_salary_premise:
    # check if the hypothesis value entails the estimate of the average salary in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the average salary
    # any value of the average salary less than or equal to 5000 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
