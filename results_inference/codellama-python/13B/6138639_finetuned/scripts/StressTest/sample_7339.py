tshirts_returned_premise = 4
tshirts_returned_hypothesis = 5

# the hypothesis talks about the number of t-shirts returned by Sanoop, referenced also in the premise
if tshirts_returned_hypothesis <= tshirts_returned_premise:
    # check if the hypothesis value contradicts the estimate of more than 'tshirts_returned_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of t-shirts returned
    # any number of t-shirts greater than 'tshirts_returned_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
