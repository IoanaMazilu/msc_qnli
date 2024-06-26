min_wage_premise = 15
min_wage_hypothesis = 15

# the hypothesis and premise mention the same minimum wage
if min_wage_hypothesis!= min_wage_premise:
    # if the minimum wage in the hypothesis does not match the minimum wage in the premise
    # then it contradicts the premise
    label = "contradiction"
else:
    # if the minimum wage in the hypothesis matches the minimum wage in the premise
    # then it is entailed by the premise
    label = "entailment"

print(label)
