tshirts_returned_premise = 2
tshirts_returned_hypothesis = 2

# the hypothesis talks about the number of t-shirts returned, which is also mentioned in the premise
if tshirts_returned_hypothesis >= tshirts_returned_premise:
    # check if the estimate of 'tshirts_returned_hypothesis' contradicts the number of t-shirts returned in the premise
    label = "contradiction"
else:
    # the premise gives exact number of t-shirts returned
    # any number of t-shirts less than 'tshirts_returned_premise' is not consistent with the premise
    label = "neutral"

print(label)
