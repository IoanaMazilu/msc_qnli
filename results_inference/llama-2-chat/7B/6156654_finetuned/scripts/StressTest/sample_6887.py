total_notes = 85
total_notes_hypothesis = 15

# the hypothesis talks about the total number of currency notes, which is also mentioned in the premise
if total_notes_hypothesis!= total_notes:
    # check if the total number of currency notes in the hypothesis contradicts the total number of currency notes in the premise
    label = "contradiction"
else:
    # if the total number of currency notes in the hypothesis does not contradict the total number of currency notes in the premise, we can infer entailment
    label = "entailment"

print(label)
