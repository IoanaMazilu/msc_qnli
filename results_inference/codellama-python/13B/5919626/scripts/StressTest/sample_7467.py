employees_premise = 100
employees_hypothesis = 100

# the premise and hypothesis refer to the same number of employees
if employees_premise!= employees_hypothesis:
    # check if the number of employees in the hypothesis contradicts the number of employees in the premise
    label = "contradiction"
else:
    # the premise and hypothesis refer to the same number of employees
    label = "entailment"

print(label)
