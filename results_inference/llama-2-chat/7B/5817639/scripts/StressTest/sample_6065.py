marks_premise = [86, 89, 82, 87, 81]
marks_hypothesis = [56, 89, 82, 87, 81]

# the hypothesis refers to the marks obtained by Dacid in the subjects mentioned in the premise
if marks_hypothesis[0] <= marks_premise[0]:
    # check if the estimate of'marks_hypothesis[0]' contradicts the number of marks obtained in English in the premise
    label = "contradiction"
elif marks_hypothesis[1]!= marks_premise[1]:
    # check if the number of marks obtained in Mathematics in the hypothesis contradicts the number of marks obtained in the premise
    label = "contradiction"
elif marks_hypothesis[2]!= marks_premise[2]:
    # check if the number of marks obtained in Physics in the hypothesis contradicts the number of marks obtained in the premise
    label = "contradiction"
elif marks_hypothesis[3]!= marks_premise[3]:
    # check if the number of marks obtained in Chemistry in the hypothesis contradicts the number of marks obtained in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
