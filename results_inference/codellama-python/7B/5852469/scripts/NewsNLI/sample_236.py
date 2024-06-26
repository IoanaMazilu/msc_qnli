employees_premise = 100
employees_hypothesis = 100

# the hypothesis mentions the number of employees in the company, which is also mentioned in the premise
if employees_hypothesis!= employees_premise:
    # check if the number of employees from the hypothesis contradicts the number of employees in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
