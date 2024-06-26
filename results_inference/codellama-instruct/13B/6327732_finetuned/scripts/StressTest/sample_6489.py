annual_borrowing_premise = 6500
annual_borrowing_hypothesis = 3500

# the hypothesis refers to the amount of money borrowed annually for college education, mentioned in the premise
if annual_borrowing_premise <= annual_borrowing_hypothesis:
    # check if the estimate of 'annual_borrowing_hypothesis' contradicts the amount of money borrowed in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
