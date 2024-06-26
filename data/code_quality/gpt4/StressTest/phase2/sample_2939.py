pens_purchased_premise = 12
pens_purchased_hypothesis = 12

# the hypothesis mentions the same number of pens purchased as the premise
if pens_purchased_hypothesis >= pens_purchased_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
