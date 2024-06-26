#bond_denomination_premise = 70
#bond_denomination_hypothesis = 50

# the hypothesis talks about the denomination of bonds, which is also mentioned in the premise
# if the denomination in the hypothesis is greater than or equal to the one in the premise, it contradicts the premise
# if the denomination in the hypothesis is less than the one in the premise, it does not contradict the premise but cannot be explicitly entailed from the premise
# if the denomination in the hypothesis is equal to the one in the premise, it contradicts the premise

#if bond_denomination_hypothesis >= bond_denomination_premise:
#    label = "contradiction"
#elif bond_denomination_hypothesis < bond_denomination_premise:
#    label = "neutral"
#else:
#    label = "entailment"

#print(label)
#