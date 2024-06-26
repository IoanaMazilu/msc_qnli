currency_notes_premise = 85
currency_notes_hypothesis = 55

# the hypothesis refers to the number of currency notes Kiran has, which is also mentioned in the premise
if currency_notes_premise <= currency_notes_hypothesis:
    # check if the number of currency notes in the premise contradicts the estimate of more than 'currency_notes_hypothesis'
    label = "contradiction"
else:
    # if the number of currency notes in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
