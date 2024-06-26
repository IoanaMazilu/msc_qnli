borrowed_pounds_premise = 6500
borrowed_pounds_hypothesis = 3500

# the hypothesis refers to the amount of money Dana borrows each year as stated in the premise
if borrowed_pounds_premise <= borrowed_pounds_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
