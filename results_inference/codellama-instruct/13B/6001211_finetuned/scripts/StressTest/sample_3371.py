tshirts_bought_premise = 8
tshirts_bought_hypothesis = 8

# the hypothesis refers to the number of t-shirts bought by Sanoop mentioned in the premise
if tshirts_bought_hypothesis <= tshirts_bought_premise:
    # check if the hypothesis value contradicts the number of t-shirts bought in the premise
    label = "contradiction"
else:
    # the premise gives the exact number of t-shirts bought
    # any number of t-shirts greater than 'tshirts_bought_premise' cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
