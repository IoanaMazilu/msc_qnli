currency_notes_premise = 85
currency_notes_hypothesis = 15

# the hypothesis talks about the number of currency notes Kiran has, referenced also in the premise
if currency_notes_hypothesis > currency_notes_premise:
    # check if the hypothesis value contradicts the estimate of 'currency_notes_premise'
    label = "contradiction"
elif currency_notes_hypothesis < currency_notes_premise:
    # check if the hypothesis value is less than the estimate of 'currency_notes_premise'
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"

print(label)
