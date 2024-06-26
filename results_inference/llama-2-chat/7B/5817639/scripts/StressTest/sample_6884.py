bond_denominations_premise = ["$50", "$100"]
bond_denominations_hypothesis = ["$70", "$100"]

# the hypothesis talks about the denominations of bonds, which is also referred to in the premise
if bond_denominations_hypothesis[0] in bond_denominations_premise:
    # check if the hypothesis value contradicts the estimate of denominations in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the denominations of bonds
    # any denomination not in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
