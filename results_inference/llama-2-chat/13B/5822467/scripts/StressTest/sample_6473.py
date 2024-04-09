average_salary_premise = 4000
average_salary_hypothesis = float(input("Enter the average salary of Raj, Roshan and Thomas: "))

# the hypothesis refers to the average salary of the three individuals
if average_salary_hypothesis <= average_salary_premise:
    # check if the estimate of the average salary in the hypothesis contradicts the premise
    label = "contradiction"
elif average_salary_hypothesis > average_salary_premise:
    # check if the average salary in the hypothesis entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the average salary
    # any salary greater than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
