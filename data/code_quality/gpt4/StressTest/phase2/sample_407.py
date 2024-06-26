borrow_rate_premise = 6
borrow_rate_hypothesis = 6

# the hypothesis talks about the interest rate at which Nitin borrowed some money, referenced also in the premise
if borrow_rate_hypothesis <= borrow_rate_premise:
    # check if the hypothesis contradicts the interest rate mentioned in the premise
    label = "contradiction"
elif borrow_rate_hypothesis > borrow_rate_premise:
    # the premise specifies the interest rate at which Nitin borrowed some money
    # any interest rate greater than 'borrow_rate_premise' cannot be explicitly entailed from the premise, thus it's neutral
    label = "neutral"

print(label)
