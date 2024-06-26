premise_salary = 4000
hypothesis_salary = 4000

# the hypothesis refers to the average salary of Raj, Roshan and Thomas
if hypothesis_salary <= premise_salary:
    # check if the estimate of 'hypothesis_salary' contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average salary
    # any average salary greater than 'premise_salary' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
