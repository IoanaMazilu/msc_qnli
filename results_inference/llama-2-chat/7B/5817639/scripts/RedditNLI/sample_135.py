number_of_banks_premise = 90
number_of_banks_hypothesis = 117

# the hypothesis and premise mention the number of banks on the problem list in two different quarters
if number_of_banks_hypothesis!= number_of_banks_premise:
    # check if the number of banks in the hypothesis contradicts the number of banks in the premise
    label = "contradiction"
else:
    # if the number of banks in the hypothesis is greater than or equal to the number of banks in the premise, we can infer entailment
    label = "entailment"

print(label)
