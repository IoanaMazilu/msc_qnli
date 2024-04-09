marks_premise = [86, 85, 82, 87, 85]
marks_hypothesis = [16, 85, 82, 87, 85]

# the hypothesis talks about the marks obtained by David in different subjects
if marks_hypothesis[0] <= marks_premise[0]:
    # check if the estimate of'marks_hypothesis[0]' contradicts the number of marks obtained in English
    label = "contradiction"
elif marks_hypothesis[1]!= marks_premise[1]:
    # check if the number of marks in Physics in the hypothesis contradicts the number of marks obtained in Physics in the premise
    label = "contradiction"
elif marks_hypothesis[2]!= marks_premise[2]:
    # check if the number of marks in Chemistry in the hypothesis contradicts the number of marks obtained in Chemistry in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
