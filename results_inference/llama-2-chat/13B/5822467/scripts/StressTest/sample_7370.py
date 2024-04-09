english_mark_premise = 55
history_mark_premise = 55
english_mark_hypothesis = 35
history_mark_hypothesis = 35

# the hypothesis refers to the averages of Suresh's marks in English and History
if english_mark_premise <= english_mark_hypothesis and history_mark_premise <= history_mark_hypothesis:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
elif english_mark_hypothesis!= english_mark_premise or history_mark_hypothesis!= history_mark_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
