annual_borrow_premise = 6500
annual_borrow_hypothesis = 3500

# the hypothesis refers to the annual amount of money borrowed by Dana for her college education, mentioned in the premise
if annual_borrow_premise <= annual_borrow_hypothesis:
    # check if the estimate of 'annual_borrow_hypothesis' contradicts the number of pounds borrowed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
