marks_premise = [16, 89, 82, 87, 81]
marks_hypothesis = [86, 89, 82, 87, 81]

# the hypothesis talks about the marks obtained by Dacid, which is also mentioned in the premise
if marks_hypothesis!= marks_premise:
    # check if the marks in the hypothesis contradict the marks mentioned in the premise
    label = "contradiction"
else:
    # if the marks in the hypothesis do not contradict the marks in the premise, we can infer entailment
    label = "entailment"

print(label)
