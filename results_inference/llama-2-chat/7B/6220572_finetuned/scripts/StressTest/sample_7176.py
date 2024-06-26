john_ Jose_Binoy_premise = 4800
john_ Jose_Binoy_hypothesis = 3800

# the hypothesis refers to the number of shares among John, Jose and Binoy mentioned in the premise
if john_ Jose_Binoy_hypothesis <= john_ Jose_Binoy_premise:
    # check if the hypothesis value contradicts the number of shares in the premise
    label = "contradiction"
else:
    # any number of shares greater than 'john_ Jose_Binoy_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
