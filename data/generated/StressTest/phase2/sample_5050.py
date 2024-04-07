# Premise: Anitha had more than 40 currency notes in all, some of which are of Rs 95 denomination and the remaining of Rs 45 denomination.
# Hypothesis: Anitha had 80 currency notes in all, some of which are of Rs 95 denomination and the remaining of Rs 45 denomination.
# Golden Label: neutral

total_notes_premise = 40
total_notes_hypothesis = 80

# the hypothesis talks about the total number of currency notes Anitha had, which is also referenced in the premise
if total_notes_hypothesis <= total_notes_premise:
    # check if the total number of notes in the hypothesis contradicts the estimate of more than 'total_notes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total number of notes
    # any total number of notes greater than 'total_notes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

