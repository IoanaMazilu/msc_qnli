premise_horses = 25
hypothesis_horses = 4

# the hypothesis refers to the number of fastest horses mentioned in the premise
if hypothesis_horses <= premise_horses:
    # check if the estimate of 'hypothesis_horses' contradicts the number of horses in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of horses
    # any number of horses greater than 'premise_horses' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
