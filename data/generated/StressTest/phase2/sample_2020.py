# Premise: If Donald carries a total of less than 65 notes (of either $10 or € 10,) then what is the total number of notes (of either $10 or € 10,) they take?
# Hypothesis: If Donald carries a total of 45 notes (of either $10 or € 10,) then what is the total number of notes (of either $10 or € 10,) they take?
# Golden Label: neutral

notes_premise = 65
notes_hypothesis = 45

# the hypothesis refers to the number of notes Donald carries, also mentioned in the premise
if notes_hypothesis >= notes_premise:
    # check if the hypothesis value contradicts the estimate of less than 'notes_premise'
    label = "contradiction"
elif notes_hypothesis < notes_premise:
    # if the number of notes in the hypothesis is less than the number in the premise, we can infer entailment
    label = "entailment"

print(label)

