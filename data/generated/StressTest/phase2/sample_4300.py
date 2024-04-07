# Premise: If Sanoop returned less than 6 t-shirts to the retailer, and the average price of the remaining t-shirts was Rs.
# Hypothesis: If Sanoop returned 1 t-shirts to the retailer, and the average price of the remaining t-shirts was Rs.
# Golden Label: neutral

tshirts_returned_premise = 6
tshirts_returned_hypothesis = 1

# the hypothesis refers to the number of t-shirts returned by Sanoop mentioned in the premise
if tshirts_returned_hypothesis >= tshirts_returned_premise:
    # check if the number of 'tshirts_returned_hypothesis' contradicts the number of t-shirts returned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of returned t-shirts
    # any number of returned t-shirts less than 'tshirts_returned_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

