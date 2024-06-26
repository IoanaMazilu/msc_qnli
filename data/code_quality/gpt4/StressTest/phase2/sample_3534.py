tshirts_bought_premise = 8
tshirts_bought_hypothesis = 3

# the hypothesis talks about the number of t-shirts bought, referenced also in the premise
if tshirts_bought_hypothesis >= tshirts_bought_premise:
    # check if the hypothesis value contradicts the exact number of 'tshirts_bought_premise'
    label = "contradiction"
else:
    # if the number of t-shirts bought in hypothesis is less than the premise, we can infer entailment
    label = "entailment"

print(label)
