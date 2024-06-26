company_employees_premise = 50
company_employees_hypothesis = 20

# the hypothesis talks about the number of employees in a company, referenced also in the premise
if company_employees_hypothesis >= company_employees_premise:
    # check if the hypothesis value contradicts the estimate of less than 'company_employees_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of employees
    # any number of employees less than 'company_employees_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
