employees_premise = 188000
employees_hypothesis = 188000

# the hypothesis talks about the number of employees in Connecticut, which is also mentioned in the premise
if employees_hypothesis!= employees_premise:
    # check if the number of employees in the hypothesis contradicts the number of employees from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)