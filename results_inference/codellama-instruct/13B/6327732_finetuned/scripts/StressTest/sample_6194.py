lexi_salary_premise = 150
lexi_salary_hypothesis = 150

# the hypothesis refers to the salary of Lexi, mentioned in the premise
if lexi_salary_hypothesis <= lexi_salary_premise:
    # check if the estimate of 'lexi_salary_hypothesis' contradicts the salary in the premise
    label = "contradiction"
else:
    # the premise gives an explicit salary for Lexi
    # any salary greater than 'lexi_salary_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
