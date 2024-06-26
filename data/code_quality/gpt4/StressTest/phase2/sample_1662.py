series_number_premise = 4
series_number_hypothesis = 2

# the hypothesis refers to a series problem number mentioned in the premise
if series_number_premise <= series_number_hypothesis:
    # check if the series number in the hypothesis contradicts the series number in the premise
    label = "contradiction"
else:
    # if the hypothesis series number does not contradict the premise series number, we can infer entailment
    label = "entailment"

print(label)
