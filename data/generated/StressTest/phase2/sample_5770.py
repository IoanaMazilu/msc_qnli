# Premise: If Donald carries a total of less than 89 notes (of either $10 or € 10,) then what is the total number of notes (of either $10 or € 10,) they take?
# Hypothesis: If Donald carries a total of 39 notes (of either $10 or € 10,) then what is the total number of notes (of either $10 or € 10,) they take?
# Golden Label: neutral

notes_premise = 89
notes_hypothesis = 39

# the hypothesis talks about the number of notes Donald carries, which is also referenced in the premise
if notes_hypothesis >= notes_premise:
    # check if the hypothesis value contradicts the premise of carrying less than 'notes_premise'
    label = "contradiction"
elif notes_hypothesis < notes_premise:
    # the premise gives an upper limit for the number of notes
    # any number of notes less than 'notes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

