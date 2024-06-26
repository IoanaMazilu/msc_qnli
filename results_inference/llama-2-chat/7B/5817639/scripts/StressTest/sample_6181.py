marks_premise = [16, 85, 82, 87, 85]
marks_hypothesis = [86, 85, 82, 87, 85]

# the hypothesis talks about the marks obtained by David in 6 subjects
if marks_hypothesis <= marks_premise:
    # check if the hypothesis value contradicts the estimate of the marks obtained by David in the premise
    label = "contradiction"
elif any(marks_hypothesis[i]!= marks_premise[i] for i in range(6)):
    # check if the marks obtained by David in the hypothesis contradict any of the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
