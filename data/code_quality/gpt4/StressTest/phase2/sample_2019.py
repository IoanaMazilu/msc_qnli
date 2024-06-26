notes_premise = 45
notes_hypothesis = 65

# the hypothesis refers to the same situation as the premise, but with a different number of notes
if notes_hypothesis <= notes_premise:
    # check if the estimate of 'notes_hypothesis' contradicts the number of notes in the premise
    label = "contradiction"
elif notes_hypothesis > notes_premise:
    # the premise gives an exact number for the notes
    # any number of notes greater than 'notes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
