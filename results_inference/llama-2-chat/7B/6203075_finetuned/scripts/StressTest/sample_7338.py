tshirts_returned_premise = 5
tshirts_returned_hypothesis = 4

# the hypothesis refers to the number of t-shirts returned by Sanoop, which is also mentioned in the premise
if tshirts_returned_hypothesis >= tshirts_returned_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, we can infer entailment
    label = "entailment"

print(label)
