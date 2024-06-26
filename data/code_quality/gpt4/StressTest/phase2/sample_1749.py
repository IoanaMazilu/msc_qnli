bonds_value_premise = 2000
bonds_value_hypothesis = 7000

# hypothesis refers to the value of US saving bonds purchased by Robert mentioned in the premise
if bonds_value_premise > bonds_value_hypothesis:
    # check if the 'bonds_value_premise' contradicts with the value of bonds in the hypothesis
    label = "contradiction"
elif bonds_value_premise == bonds_value_hypothesis:
    # check if the 'bonds_value_premise' is equal to the value of bonds in the hypothesis
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis value, it can be inferred as entailment
    label = "entailment"

print(label)
