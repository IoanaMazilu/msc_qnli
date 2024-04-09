tshirts_bought_premise = 8
tshirts_bought_hypothesis = 8

# the hypothesis refers to the number of t-shirts bought by Sanoop mentioned in the premise
if tshirts_bought_hypothesis >= tshirts_bought_premise:
    # check if the hypothesis value contradicts the number of t-shirts bought in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
