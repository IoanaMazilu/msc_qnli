tshirts_bought_premise = 8
tshirts_bought_hypothesis = 8

# the hypothesis talks about the number of t-shirts bought by Sanoop, referenced also in the premise
if tshirts_bought_hypothesis < tshirts_bought_premise:
    # check if the hypothesis value contradicts the number of t-shirts bought by Sanoop in the premise
    label = "contradiction"
elif tshirts_bought_hypothesis == tshirts_bought_premise:
    # the premise and hypothesis are the same
    # but the hypothesis suggests that the number of t-shirts bought by Sanoop should be more than the premise
    label = "contradiction"
else:
    # any number of t-shirts bought by Sanoop greater than 'tshirts_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
