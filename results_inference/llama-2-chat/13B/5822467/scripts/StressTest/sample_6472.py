average_salary_premise = float(input("Enter the average salary of Raj, Roshan and Thomas in the premise: "))
average_salary_hypothesis = float(input("Enter the average salary of Raj, Roshan and Thomas in the hypothesis: "))

# the hypothesis refers to the average salary of Raj, Roshan and Thomas mentioned in the premise
if average_salary_premise <= average_salary_hypothesis:
    # check if the estimate of 'average_salary_hypothesis' contradicts the premise
    label = "contradiction"
elif average_salary_hypothesis!= average_salary_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
