premise = "If bonds are sold in $50 or $100 denominations only, which of the following CAN NOT be the number of US saving bonds that Robert purchased?"
hypothesis = "If bonds are sold in $10 or $100 denominations only, which of the following CAN NOT be the number of US saving bonds that Robert purchased?"

# extract the numerical entities from the premise and hypothesis
premise_bonds = premise.split(" ")[-1]
hypothesis_bonds = hypothesis.split(" ")[-1]

# check if the hypothesis value contradicts the premise value
if hypothesis_bonds <= premise_bonds:
    label = "contradiction"
else:
    label = "neutral"

print(label)
