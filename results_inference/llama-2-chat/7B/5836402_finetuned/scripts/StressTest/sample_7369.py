average_marks_premise = 15
average_marks_hypothesis = 55

# the hypothesis refers to the average marks of Suresh in English and History mentioned in the premise
if average_marks_hypothesis <= average_marks_premise:
    # check if the estimate of 'average_marks_hypothesis' contradicts the average marks in the premise
    label = "contradiction"
elif average_marks_hypothesis > average_marks_premise:
    # check if the average marks in the hypothesis contradicts the average marks reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
