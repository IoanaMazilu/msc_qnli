currency_notes_premise = 85
currency_notes_hypothesis = 15

# the hypothesis refers to the number of currency notes Kiran has, which is also mentioned in the premise
if currency_notes_hypothesis!= currency_notes_premise:
    # check if the number of currency notes in the hypothesis contradicts the number of currency notes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
