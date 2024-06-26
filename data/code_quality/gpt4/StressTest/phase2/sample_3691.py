bonds_value_premise = 6000
bonds_value_hypothesis = 1000

# the hypothesis refers to the value of US saving bonds purchased by Robert, also mentioned in the premise
if bonds_value_hypothesis >= bonds_value_premise:
    # check if the value of bonds in the hypothesis contradicts the estimate of less than 'bonds_value_premise'
    label = "contradiction"
elif bonds_value_hypothesis < bonds_value_premise:
    # any value of bonds less than 'bonds_value_premise' is consistent with the premise and can be entailed from the premise
    label = "entailment"

print(label)
