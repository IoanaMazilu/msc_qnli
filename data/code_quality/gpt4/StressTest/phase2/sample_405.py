borrow_rate_premise = 6
borrow_rate_hypothesis = 1

# the hypothesis refers to the borrowing rate mentioned in the premise
if borrow_rate_premise <= borrow_rate_hypothesis:
    # check if the 'borrow_rate_hypothesis' contradicts the borrowing rate in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
