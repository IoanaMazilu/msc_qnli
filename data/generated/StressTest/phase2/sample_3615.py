# Premise: If Donald carries a total of 33 notes (of either $10 or € 10,) then what is the total number of notes (of either $10 or € 10,) they take?
# Hypothesis: If Donald carries a total of more than 13 notes (of either $10 or € 10,) then what is the total number of notes (of either $10 or € 10,) they take?
# Golden Label: entailment

notes_premise = 33
notes_hypothesis = 13

# the hypothesis refers to the number of notes carried by Donald, mentioned also in the premise
if notes_premise <= notes_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, it can be entailed from the premise
    label = "entailment"

print(label)

