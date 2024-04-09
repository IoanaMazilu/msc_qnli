bond_denominations_premise = 70
bond_denominations_hypothesis = 50

# the hypothesis talks about the number of bond denominations, referenced also in the premise
if bond_denominations_hypothesis <= bond_denominations_premise:
    # check if the hypothesis value contradicts the estimate of less than 'bond_denominations_premise'
    label = "contradiction"
elif bond_denominations_premise == bond_denominations_hypothesis:
    # check if the hypothesis value is consistent with the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the number of bond denominations
    # any number of bond denominations less than or equal to 'bond_denominations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
