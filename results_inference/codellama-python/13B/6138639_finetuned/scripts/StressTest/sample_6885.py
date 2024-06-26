currency_notes_premise = 85
currency_notes_hypothesis = 55

# the hypothesis refers to the number of currency notes Kiran has, which is also mentioned in the premise
if currency_notes_premise <= currency_notes_hypothesis:
    # check if the estimate of 'currency_notes_hypothesis' contradicts the number of currency notes in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
