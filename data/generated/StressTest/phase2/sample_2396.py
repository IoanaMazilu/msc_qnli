# Premise: If Sanoop returned 3 t-shirts to the retailer, and the average price of the remaining t-shirts was Rs.
# Hypothesis: If Sanoop returned less than 3 t-shirts to the retailer, and the average price of the remaining t-shirts was Rs.
# Golden Label: contradiction

tshirts_returned_premise = 3
tshirts_returned_hypothesis = 3

# the hypothesis refers to the number of t-shirts returned by Sanoop mentioned in the premise
if tshirts_returned_hypothesis >= tshirts_returned_premise:
    # check if the hypothesis value contradicts the number of t-shirts returned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

