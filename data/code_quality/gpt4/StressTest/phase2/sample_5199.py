annual_borrow_premise = 4000
annual_borrow_hypothesis = 1000

# the hypothesis refers to the annual amount of money borrowed by Dana for her college education, mentioned also in the premise
if annual_borrow_premise <= annual_borrow_hypothesis:
    # check if the stated 'annual_borrow_hypothesis' contradicts the annual amount of money borrowed in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
