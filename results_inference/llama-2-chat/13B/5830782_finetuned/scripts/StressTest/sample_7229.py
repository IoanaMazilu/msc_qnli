marks_premise = [66, 75, 52, 68, 89]
marks_hypothesis = [86, 75, 52, 68, 89]

# the hypothesis talks about the marks obtained by Nancy, referenced also in the premise
if marks_hypothesis!= marks_premise:
    # check if the marks in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the marks in the hypothesis do not contradict the marks in the premise, we can infer entailment
    label = "entailment"

print(label)
