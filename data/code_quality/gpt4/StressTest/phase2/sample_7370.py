average_marks_premise = 55
average_marks_hypothesis = 35

# the hypothesis refers to the average of Suresh's marks in English and History mentioned in the premise
if average_marks_hypothesis != average_marks_premise:
    # check if the average marks in the hypothesis contradicts the average marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values are the same as the premise ones, we can infer entailment
    label = "entailment"

print(label)
