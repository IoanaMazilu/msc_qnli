dan_work_hours_premise = 8
dan_work_hours_hypothesis = 3

# the hypothesis references the number of hours Dan works alone, mentioned also in the premise
if dan_work_hours_premise <= dan_work_hours_hypothesis:
    # check if the number of hours in the hypothesis contradicts the number of hours Dan works alone in the premise
    label = "contradiction"
else:
    # if the hypothesis hours estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
