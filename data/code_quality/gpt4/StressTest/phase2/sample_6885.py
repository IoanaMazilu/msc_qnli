currency_notes_premise = 85
currency_notes_hypothesis = 55

# the hypothesis talks about the total number of currency notes Kiran has, which is also mentioned in the premise
if currency_notes_premise < currency_notes_hypothesis:
    # check if the premise value contradicts the estimate of more than 'currency_notes_hypothesis'
    label = "contradiction"
elif currency_notes_hypothesis > currency_notes_premise:
    # check if the number of currency notes in the hypothesis contradicts the number of currency notes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
