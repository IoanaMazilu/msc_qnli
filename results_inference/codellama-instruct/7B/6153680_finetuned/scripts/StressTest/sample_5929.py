marks_premise = [46, 85, 92, 87, 95]
marks_hypothesis = [86, 85, 92, 87, 95]

# the hypothesis talks about the marks obtained by Dacid, which is also mentioned in the premise
if marks_hypothesis <= marks_premise:
    # check if the marks in the hypothesis contradict the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
