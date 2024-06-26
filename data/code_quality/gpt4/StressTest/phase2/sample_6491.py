annual_borrow_premise = 6500
annual_borrow_hypothesis = 1500

# the hypothesis talks about the annual amount of money Dana borrows for college, which is also mentioned in the premise
if annual_borrow_hypothesis == annual_borrow_premise:
    # check if the annual borrow amount in the hypothesis is exactly the same as the one stated in the premise
    label = "entailment"
elif annual_borrow_hypothesis > annual_borrow_premise:
    # check if the annual borrow amount in the hypothesis is greater than the one stated in the premise
    label = "contradiction"
else:
    # the premise gives a specific amount for the annual borrow, any lower amount in the hypothesis does not contradict the premise
    # but it cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
