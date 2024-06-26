saved_salary_premise = 10
saved_salary_hypothesis = 40

# the hypothesis refers to the percentage of the salary saved by Kishore, also mentioned in the premise
if saved_salary_premise >= saved_salary_hypothesis:
    # check if 'saved_salary_premise' contradicts the hypothesis estimation of less than 'saved_salary_hypothesis'
    label = "contradiction"
elif saved_salary_hypothesis != saved_salary_premise:
    # the premise gives only an exact percentage of the salary saved
    # any percentage less than 'saved_salary_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
