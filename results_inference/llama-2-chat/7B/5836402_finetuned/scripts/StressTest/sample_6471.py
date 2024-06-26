average_salary_premise = 4000
average_salary_hypothesis = 5000

# the hypothesis refers to the average salary of Raj, Roshan and Thomas mentioned in the premise
if average_salary_premise >= average_salary_hypothesis:
    # check if the estimate of 'average_salary_hypothesis' contradicts the average salary in the premise
    label = "contradiction"
elif average_salary_hypothesis < average_salary_premise:
    # check if the estimate of 'average_salary_hypothesis' is less than the average salary in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
