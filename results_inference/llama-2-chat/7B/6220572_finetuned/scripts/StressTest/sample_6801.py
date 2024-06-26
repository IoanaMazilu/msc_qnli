bond_denominations_premise = [50, 100]
bond_denominations_hypothesis = [70, 100]

# the hypothesis refers to the bond denominations mentioned in the premise
if bond_denominations_hypothesis[0] <= bond_denominations_premise[0]:
    # check if the hypothesis estimate contradicts the premise estimate of $50 or $100 denominations
    label = "contradiction"
elif bond_denominations_hypothesis[1] <= bond_denominations_premise[1]:
    # check if the hypothesis estimate contradicts the premise estimate of $100 denominations
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of bonds purchased
    # any number of bonds consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
