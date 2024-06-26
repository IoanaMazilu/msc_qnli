marks_obtained_premise = [86, 75, 52, 68, 89]
marks_obtained_hypothesis = [66, 75, 52, 68, 89]

# the hypothesis talks about the marks obtained by Nancy in the same subjects as the premise
if marks_obtained_hypothesis!= marks_obtained_premise:
    # check if the marks obtained in the hypothesis contradict the marks obtained in the premise
    label = "contradiction"
else:
    # if the marks obtained in the hypothesis do not contradict the marks obtained in the premise, we can infer entailment
    label = "entailment"

print(label)
