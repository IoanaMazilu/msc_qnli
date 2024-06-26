pencils_premise = 125
pencils_hypothesis = 525

# the hypothesis refers to the number of pencils owned by Shreehari, mentioned in the premise
if pencils_premise <= pencils_hypothesis:
    # check if the estimate of 'pencils_hypothesis' contradicts the number of pencils reported in the premise
    label = "contradiction"
else:
    # the premise gives a specific number of pencils, while the hypothesis gives a much larger number
    # any number of pencils greater than 'pencils_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
