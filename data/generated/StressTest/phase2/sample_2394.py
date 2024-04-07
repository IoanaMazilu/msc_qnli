# Premise: If Sanoop returned 3 t-shirts to the retailer, and the average price of the remaining t-shirts was Rs.
# Hypothesis: If Sanoop returned less than 8 t-shirts to the retailer, and the average price of the remaining t-shirts was Rs.
# Golden Label: entailment

tshirts_returned_premise = 3
tshirts_returned_hypothesis = 8

# the hypothesis refers to the number of t-shirts returned by Sanoop mentioned in the premise
if tshirts_returned_hypothesis < tshirts_returned_premise:
    # check if the number of 'tshirts_returned_hypothesis' contradicts the number of t-shirts returned in the premise
    label = "contradiction"
elif tshirts_returned_hypothesis > tshirts_returned_premise:
    # the premise tells us exactly how many t-shirts were returned
    # any number of returned t-shirts greater than 'tshirts_returned_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

