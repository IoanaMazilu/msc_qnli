# define variables with representative names for the numerical entities in both inputs
mani_rani_share_premise = 200
mani_rani_share_hypothesis = 200

# extract all quantities as valid numbers (integers or floats)
mani_rani_share_premise = int(mani_rani_share_premise)
mani_rani_share_hypothesis = int(mani_rani_share_hypothesis)

# use brief comments to explain what comparison you do between the defined variables
if mani_rani_share_hypothesis > mani_rani_share_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference between Mani and Rani's share
    # any number greater than'mani_rani_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
