jim_stretch_premise = 30
jim_stretch_hypothesis = 80

# the hypothesis refers to the time Jim stops to stretch, which is mentioned in the premise
if jim_stretch_premise <= jim_stretch_hypothesis:
    # check if the estimate of 'jim_stretch_hypothesis' contradicts the time Jim stops to stretch in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Jim stops to stretch
    # any time greater than 'jim_stretch_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
