# Premise: Nitin borrowed some money at the rate of 6% p.
# Hypothesis: Nitin borrowed some money at the rate of less than 6% p.
# Golden Label: contradiction

borrow_rate_premise = 6
borrow_rate_hypothesis = 6

# the hypothesis talks about the rate of borrowing money, which is also mentioned in the premise
if borrow_rate_hypothesis >= borrow_rate_premise:
    # check if the hypothesis rate contradicts the premise rate
    label = "contradiction"
else:
    # the premise gives a specific borrowing rate
    # a borrowing rate less than 'borrow_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

