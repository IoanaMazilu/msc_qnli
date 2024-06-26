tshirts_bought_premise = 8
tshirts_bought_hypothesis = 8

# the hypothesis talks about the number of t-shirts bought, which is also mentioned in the premise
if tshirts_bought_hypothesis >= tshirts_bought_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif tshirts_bought_hypothesis < tshirts_bought_premise:
    # if the hypothesis value is less than the premise value, it is consistent with the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it is neutral
    label = "neutral"

print(label)
