total_salary_premise = 4000
total_salary_hypothesis = 4000
average_salary_premise = 0
average_salary_hypothesis = 0

# the hypothesis refers to the total salary and average salary of Raj, Roshan and Thomas, mentioned in the premise
if total_salary_premise <= total_salary_hypothesis:
    # check if the estimate of 'total_salary_hypothesis' contradicts the total salary in the premise
    label = "contradiction"
elif average_salary_hypothesis!= average_salary_premise:
    # check if the average salary in the hypothesis contradicts the average salary reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
