average_salary_premise = 4000
average_salary_hypothesis = 4000

# the hypothesis talks about the average salary of Raj, Roshan and Thomas, which is also mentioned in the premise
if average_salary_hypothesis >= average_salary_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives an exact value for the average salary
    # any value greater than 'average_salary_premise' contradicts the premise
    label = "contradiction"

print(label)
