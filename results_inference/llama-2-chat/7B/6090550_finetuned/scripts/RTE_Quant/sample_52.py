employees_premise = 188000
employees_hypothesis = 188000

# the hypothesis mentions the number of employees in the state, which is also mentioned in the premise
if employees_hypothesis!= employees_premise:
    # check if the number of employees in the hypothesis contradicts the number of employees in the premise
    label = "contradiction"
else:
    # if the number of employees in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
