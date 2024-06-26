tshirts_bought_premise = 4
tshirts_bought_hypothesis = 8

# the hypothesis talks about the number of t-shirts Sanoop bought, referenced also in the premise
if tshirts_bought_hypothesis <= tshirts_bought_premise:
    # check if the hypothesis value contradicts the estimate of more than 'tshirts_bought_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of t-shirts
    # any number of t-shirts greater than 'tshirts_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
