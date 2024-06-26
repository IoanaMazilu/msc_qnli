average_marks_premise = 55
average_marks_hypothesis = 15

# the hypothesis talks about the average marks in English and History of Suresh, which is also mentioned in the premise
if average_marks_premise < average_marks_hypothesis:
    # check if the hypothesis value contradicts the premise average_marks
    label = "contradiction"
elif average_marks_hypothesis != average_marks_premise:
    # check if the average marks in the hypothesis contradicts the average marks reported in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
