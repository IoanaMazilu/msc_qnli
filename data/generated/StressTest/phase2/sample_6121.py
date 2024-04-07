# Premise: If Sanoop returned less than 8 t-shirts to the retailer, and the average price of the remaining t-shirts was Rs.
# Hypothesis: If Sanoop returned 4 t-shirts to the retailer, and the average price of the remaining t-shirts was Rs.
# Golden Label: neutral

tshirts_returned_premise = 8
tshirts_returned_hypothesis = 4

# the hypothesis talks about the number of t-shirts returned by Sanoop, referenced also in the premise
if tshirts_returned_hypothesis >= tshirts_returned_premise:
    # check if the hypothesis value contradicts the estimate of less than 'tshirts_returned_premise'
    label = "contradiction"
elif tshirts_returned_hypothesis < tshirts_returned_premise:
    # any number of returned t-shirts less than 'tshirts_returned_premise' is consistent with the premise, it can be explicitly entailed from the premise
    label = "entailment"
else:
    # if the values in the hypothesis do not contradict or affirm the premise ones, we can infer neutrality
    label = "neutral"

print(label)

