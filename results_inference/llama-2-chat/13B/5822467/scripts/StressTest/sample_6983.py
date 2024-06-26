borrowed_money_premise = 6
borrowed_money_hypothesis = 8

# the hypothesis refers to the interest rate at which Nitin borrowed money
if borrowed_money_hypothesis <= borrowed_money_premise:
    # check if the hypothesis value contradicts the estimate of 6% p.
    label = "contradiction"
elif borrowed_money_premise!= borrowed_money_hypothesis:
    # check if the hypothesis value contradicts the estimate of 6% p.
    label = "contradiction"
else:
    # if the hypothesis value and the premise estimate do not contradict, we can infer neutrality
    label = "neutral"

print(label)
