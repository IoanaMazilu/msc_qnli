premise_salary = 4000
hypothesis_salary = 5000

# the hypothesis talks about the average salary of Raj, Roshan and Thomas
# the premise gives only an estimate for the average salary
if hypothesis_salary <= premise_salary:
    # check if the hypothesis value contradicts the estimate of less than 'premise_salary'
    label = "contradiction"
else:
    # any number of salary greater than 'premise_salary' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
