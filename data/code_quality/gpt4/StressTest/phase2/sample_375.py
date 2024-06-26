borrow_rate_premise = 6
borrow_rate_hypothesis = 3

# the hypothesis refers to the borrowing rate mentioned in the premise
if borrow_rate_premise <= borrow_rate_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif borrow_rate_premise > borrow_rate_hypothesis:
    # check if the premise value is greater than the hypothesis value
    label = "entailment"
else:
    # if the hypothesis value does not contradict the premise value, we can infer it is neutral
    label = "neutral"

print(label)
