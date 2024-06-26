# define variables for the numerical entities in the premise and hypothesis
premise_price = 3
hypothesis_price = 3

# extract all quantities as valid numbers
premise_price = float(premise_price)
hypothesis_price = float(hypothesis_price)

# use brief comments to explain what comparison you do between the defined variables
if premise_price!= hypothesis_price:
    # check if the price in the premise contradicts the price in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
