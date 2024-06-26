 shopping_premise = 6
shopping_hypothesis = 1

# the hypothesis talks about the number of ball Amanda is going to buy, which is also referenced in the premise
if shopping_hypothesis >= shopping_premise:
    # check if the hypothesis value contradicts the estimate of less than'shopping_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of ball Amanda is going to buy
    # any number of ball less than'shopping_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
