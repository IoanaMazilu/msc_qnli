premise = 31
hypothesis = 41

# the hypothesis refers to the number of people who have visited both Iceland and Norway
if premise <= hypothesis:
    # check if the hypothesis value contradicts the number of people mentioned in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of people who have visited both Iceland and Norway
    # any number of people greater than 'premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
