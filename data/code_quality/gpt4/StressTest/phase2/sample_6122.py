tshirts_returned_premise = 4
tshirts_returned_hypothesis = 8

# the hypothesis refers to the number of t-shirts returned by Sanoop, mentioned also in the premise
if tshirts_returned_hypothesis != tshirts_returned_premise:
    # check if the number of t-shirts returned in the hypothesis contradicts the number of t-shirts returned in the premise
    label = "contradiction"
else:
    # as there is no information about the average price of the remaining t-shirts in either premise or hypothesis, we can't conclude anything about it
    label = "neutral"

print(label)
