anwar_premise = 3600
anwar_hypothesis = 1600

if anwar_premise <= anwar_hypothesis:
    # check if the hypothesis value contradicts the number of Anwar's contribution in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Anwar's contribution
    # any number of Anwar's contribution greater than 'anwar_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
