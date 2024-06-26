notes_premise = 85
notes_hypothesis = 55

# the hypothesis refers to the number of currency notes mentioned in the premise
if notes_premise <= notes_hypothesis:
    # check if the estimate of 'notes_hypothesis' contradicts the number of currency notes in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of currency notes
    # any number of currency notes greater than 'notes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
