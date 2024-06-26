notes_premise = 40
notes_hypothesis = 30

# the hypothesis talks about the total number of notes carried by Donald, referenced also in the premise
if notes_hypothesis >= notes_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'notes_premise'
    label = "contradiction"
elif notes_hypothesis < notes_premise:
    # if the number of notes in the hypothesis is less than 'notes_premise', it can be explicitly entailed from the premise
    label = "entailment"

print(label)
