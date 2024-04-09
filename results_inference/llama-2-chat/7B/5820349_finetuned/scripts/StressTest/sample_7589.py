average_marks_premise = [86, 75, 72, 63, 65]
average_marks_hypothesis = [86, 75, 72, 63, 65]

# the hypothesis refers to the average marks scored by Adam in the same subjects mentioned in the premise
if average_marks_hypothesis[0] <= average_marks_premise[0]:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif average_marks_hypothesis[1]!= average_marks_premise[1]:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif average_marks_hypothesis[2]!= average_marks_premise[2]:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif average_marks_hypothesis[3]!= average_marks_premise[3]:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif average_marks_hypothesis[4]!= average_marks_premise[4]:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
