salary_premise = 1200
salary_hypothesis = 3200

# the hypothesis talks about Mary's monthly salary, also referenced in the premise
if salary_hypothesis == salary_premise:
    # check if the hypothesis value contradicts the salary reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the salary
    # any salary greater than'salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
