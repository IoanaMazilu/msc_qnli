# Premise: If Donald carries a total of 33 notes (of either $10 or € 10,) then what is the total number of notes (of either $10 or € 10,) they take?
# Hypothesis: If Donald carries a total of more than 33 notes (of either $10 or € 10,) then what is the total number of notes (of either $10 or € 10,) they take?
# Golden Label: contradiction

notes_donald_premise = 33
notes_donald_hypothesis = 33

# the hypothesis talks about the number of notes Donald is carrying, as does the premise
if notes_donald_hypothesis > notes_donald_premise:
    # check if the hypothesis value contradicts the exact number 'notes_donald_premise'
    label = "contradiction"
elif notes_donald_hypothesis < notes_donald_premise:
    # check if the hypothesis value contradicts the exact number 'notes_donald_premise'
    label = "contradiction"
else:
    # the exact number of notes Donald is carrying is given in the premise
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

