number_banks_premise = 30
number_banks_hypothesis = 117

# the hypothesis and premise mention the number of banks on the problem list
if number_banks_hypothesis < number_banks_premise:
    # check if the number of banks in the hypothesis contradicts the number of banks in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of banks
    # any estimate of the number of banks in the hypothesis greater or equal to 'number_banks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
