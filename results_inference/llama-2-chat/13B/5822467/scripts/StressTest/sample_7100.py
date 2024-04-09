marks_premise = 66
marks_hypothesis = 36

# the hypothesis refers to the marks secured by Reema, which is mentioned in the premise
if marks_premise <= marks_hypothesis:
    # check if the estimate of'marks_hypothesis' contradicts the value of marks secured by Reema in the premise
    label = "contradiction"
elif marks_hypothesis > marks_premise:
    # check if the hypothesis value contradicts the value of marks secured by Reema in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
