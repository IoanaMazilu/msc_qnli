meg_bob_premise = 7
meg_bob_hypothesis = 8

# the hypothesis refers to the number of participants in the cycling race, mentioned in the premise
if meg_bob_premise <= meg_bob_hypothesis:
    # check if the hypothesis value contradicts the number of participants reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of participants
    # any number of participants less than or equal to 8 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
