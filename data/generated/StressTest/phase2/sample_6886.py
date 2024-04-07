# Premise: Kiran has more than 55 currency notes in all, some of which were of Rs.
# Hypothesis: Kiran has 85 currency notes in all, some of which were of Rs.
# Golden Label: neutral

notes_premise = 55
notes_hypothesis = 85

# the hypothesis refers to the total number of currency notes Kiran has, which is also mentioned in the premise
if notes_hypothesis <= notes_premise:
    # check if the total number of notes in the hypothesis contradicts the estimation of more than 'notes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of notes
    # any number of notes greater than 'notes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

