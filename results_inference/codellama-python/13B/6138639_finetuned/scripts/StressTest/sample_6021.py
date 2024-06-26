annual_borrow_premise = 5000
annual_borrow_hypothesis = 2000

# the hypothesis refers to the annual borrowing amount mentioned in the premise
if annual_borrow_premise <= annual_borrow_hypothesis:
    # check if the estimate of 'annual_borrow_hypothesis' contradicts the amount of annual borrowing in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
