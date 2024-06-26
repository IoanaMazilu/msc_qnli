amount_premise = 3600

# the hypothesis talks about the amount from Anwar at 6% p., referenced also in the premise
if amount_premise <= amount_hypothesis:
    # check if the hypothesis value contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise amount, we can infer entailment
    label = "entailment"

print(label)
