borrow_rate_premise = 6
borrow_rate_hypothesis = 5

# the hypothesis talks about the rate at which Nitin borrowed money, referenced also in the premise
if borrow_rate_premise <= borrow_rate_hypothesis:
    # check if the premise value contradicts the estimate of more than 'borrow_rate_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
