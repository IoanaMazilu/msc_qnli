marks_premise = [66, 75, 52, 68, 89]
marks_hypothesis = [86, 75, 52, 68, 89]

# the hypothesis talks about the marks obtained by Nancy in the same subjects as in the premise
if marks_hypothesis!= marks_premise:
    # check if the marks in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
