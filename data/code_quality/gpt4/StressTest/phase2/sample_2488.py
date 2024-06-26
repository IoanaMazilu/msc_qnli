salary_premise = 7550
salary_hypothesis = 4550

# the hypothesis refers to the salary Thomas earns per week in the factory, mentioned also in the premise
if salary_hypothesis >= salary_premise:
    # check if the hypothesis value contradicts the estimate of less than 'salary_premise'
    label = "contradiction"
elif salary_hypothesis < salary_premise:
    # any salary less than 'salary_premise' is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)
