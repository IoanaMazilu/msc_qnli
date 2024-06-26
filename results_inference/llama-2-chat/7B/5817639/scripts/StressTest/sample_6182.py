marks_premise = [86, 85, 82, 87, 85]
marks_hypothesis = [85, 84, 83, 82, 81]

# the hypothesis talks about the marks obtained by David in different subjects
if marks_hypothesis[0] <= marks_premise[0]:
    # check if the estimate of'marks_hypothesis[0]' contradicts the actual mark in the premise
    label = "contradiction"
elif marks_hypothesis[1]!= marks_premise[1]:
    # check if the estimate of'marks_hypothesis[1]' contradicts the actual mark in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
