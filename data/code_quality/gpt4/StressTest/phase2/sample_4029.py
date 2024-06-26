notes_premise = 100
notes_hypothesis = 300

# the hypothesis talks about the total number of currency notes with Gokul, referenced also in the premise
if notes_hypothesis < notes_premise:
    # check if the hypothesis value contradicts the exact number of 'notes_premise'
    label = "contradiction"
elif notes_hypothesis == notes_premise:
    # if the number of notes in the hypothesis is equal to the number of notes in the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives an exact number for the total notes
    # any number of notes less than 'notes_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
