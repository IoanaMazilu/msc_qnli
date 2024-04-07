# Premise: If Donald carries a total of 45 notes (of either $10 or € 10,) then what is the total number of notes (of either $10 or € 10,) they take?
# Hypothesis: If Donald carries a total of more than 45 notes (of either $10 or € 10,) then what is the total number of notes (of either $10 or € 10,) they take?
# Golden Label: contradiction

notes_premise = 45
notes_hypothesis = 45

# the hypothesis talks about the number of notes Donald carries, referenced also in the premise
if notes_hypothesis != notes_premise:
    # check if the hypothesis value contradicts the number of notes in the premise
    label = "contradiction"
else:
    # if hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

