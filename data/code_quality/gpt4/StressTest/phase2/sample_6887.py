notes_premise = 85
notes_hypothesis = 15

# the hypothesis talks about the number of currency notes Kiran has, referenced also in the premise
if notes_hypothesis != notes_premise:
    # check if the number of notes in the hypothesis contradicts the number of notes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
