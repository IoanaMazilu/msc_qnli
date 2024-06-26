toys_purchased_premise = 10
toys_purchased_hypothesis = 20

# the hypothesis talks about the number of dozens of toys purchased by Sam, referenced also in the premise
if toys_purchased_hypothesis <= toys_purchased_premise:
    # check if the hypothesis value contradicts the estimate of more than 'toys_purchased_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of dozens of toys
    # any number of dozens of toys greater than 'toys_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
