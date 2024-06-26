notes_premise = 55
notes_hypothesis = 85

# the hypothesis talks about the number of currency notes Kiran has, referenced also in the premise
if notes_hypothesis <= notes_premise:
    # check if the hypothesis value contradicts the estimate of more than 'notes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of currency notes
    # any number of currency notes greater than 'notes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
