# Premise: If Sanoop returned 5 t-shirts to the retailer, and the average price of the remaining t-shirts was Rs.
# Hypothesis: If Sanoop returned more than 4 t-shirts to the retailer, and the average price of the remaining t-shirts was Rs.
# Golden Label: entailment

tshirts_returned_premise = 5
tshirts_returned_hypothesis = 4

# the hypothesis refers to the number of returned t-shirts mentioned in the premise
if tshirts_returned_hypothesis >= tshirts_returned_premise:
    # check if the 'tshirts_returned_hypothesis' contradicts the number of returned t-shirts in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

