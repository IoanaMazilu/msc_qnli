tshirts_returned_premise = 4
tshirts_returned_hypothesis = 5

# the hypothesis refers to the number of t-shirts returned by Sanoop, which is also mentioned in the premise
if tshirts_returned_hypothesis >= tshirts_returned_premise:
    # check if the number of t-shirts returned in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
