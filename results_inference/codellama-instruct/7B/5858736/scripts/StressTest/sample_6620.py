jane_thomas_premise = 7
jane_thomas_hypothesis = 7
committee_size = 4

# the hypothesis refers to the number of people from which the committee is to be selected
if jane_thomas_premise <= committee_size:
    # check if the estimate of 'jane_thomas_hypothesis' contradicts the number of people mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people from which the committee is to be selected
    # any number of people greater than 'jane_thomas_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
