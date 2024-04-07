# Premise: If Sanoop returned less than 8 t-shirts to the retailer, and the average price of the remaining t-shirts was Rs.
# Hypothesis: If Sanoop returned 3 t-shirts to the retailer, and the average price of the remaining t-shirts was Rs.
# Golden Label: neutral

tshirts_returned_premise = 8
tshirts_returned_hypothesis = 3

# the hypothesis states a specific number of returned t-shirts, which is also mentioned in the premise
if tshirts_returned_hypothesis >= tshirts_returned_premise:
    # check if the hypothesis value contradicts the premise's limit of less than 'tshirts_returned_premise'
    label = "contradiction"
elif tshirts_returned_hypothesis < tshirts_returned_premise:
    # if the hypothesis value is less than the premise's limit, it does not contradict the premise
    # but since the premise only gives a limit, the specific number in the hypothesis cannot be explicitly entailed
    label = "neutral"

print(label)

