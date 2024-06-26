tshirts_returned_premise = 3
tshirts_returned_hypothesis = 2

# the hypothesis refers to the number of t-shirts returned by Sanoop, as mentioned in the premise
if tshirts_returned_hypothesis >= tshirts_returned_premise:
    # check if the number of t-shirts returned in the hypothesis contradicts the estimate of less than 'tshirts_returned_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    # note: the average price of the remaining t-shirts is not given in either sentences, thus it cannot be included in the comparison
    label = "entailment"

print(label)
