annual_borrow_premise = 6500
annual_borrow_hypothesis = 3500

# the hypothesis refers to the annual amount of money borrowed by Dana for college, which is also mentioned in the premise
if annual_borrow_premise <= annual_borrow_hypothesis:
    # check if the estimate of 'annual_borrow_hypothesis' contradicts the amount of money borrowed annually in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)