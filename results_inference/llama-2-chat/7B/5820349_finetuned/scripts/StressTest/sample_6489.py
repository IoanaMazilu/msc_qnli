annual_borrow_premise = 6500
annual_borrow_hypothesis = 3500

# the hypothesis refers to the annual amount Dana borrows for her college, which is also mentioned in the premise
if annual_borrow_premise <= annual_borrow_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
