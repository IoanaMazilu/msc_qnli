currency_notes_premise = 85
currency_notes_hypothesis = 15

# the hypothesis talks about the number of currency notes Kiran has, referenced also in the premise
if currency_notes_hypothesis <= currency_notes_premise:
    # check if the hypothesis value contradicts the number of currency notes in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of currency notes
    # any number of currency notes greater than 'currency_notes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
