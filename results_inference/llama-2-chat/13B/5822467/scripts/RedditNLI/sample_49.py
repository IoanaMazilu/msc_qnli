premise_debt = 570000000000
hypothesis_debt = 570000000000

# the premise and hypothesis mention the amount of global debt in trillions of dollars
if premise_debt!= hypothesis_debt:
    # check if the amount of debt in the hypothesis contradicts the premise
    label = "contradiction"
elif hypothesis_debt > premise_debt:
    # check if the amount of debt in the hypothesis entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the amount of debt
    # any estimate of the amount of debt in the hypothesis greater or equal to the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
