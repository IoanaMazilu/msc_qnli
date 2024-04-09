currency_notes_premise = 85
currency_notes_hypothesis = 55

# the hypothesis refers to the total number of currency notes and some of them being of Rs.
if currency_notes_hypothesis <= currency_notes_premise:
    # check if the estimate of 'currency_notes_hypothesis' contradicts the number of currency notes reported in the premise
    label = "contradiction"
elif currency_notes_premise!= currency_notes_hypothesis:
    # check if the number of currency notes in the hypothesis contradicts the number of currency notes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
