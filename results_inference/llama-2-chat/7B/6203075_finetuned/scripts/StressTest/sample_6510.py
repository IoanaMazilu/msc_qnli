product_premise = 7
product_hypothesis = 5

# the hypothesis talks about a product of X, Y and Z, which is also mentioned in the premise
if product_hypothesis <= product_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, we can infer entailment
    label = "entailment"

print(label)
