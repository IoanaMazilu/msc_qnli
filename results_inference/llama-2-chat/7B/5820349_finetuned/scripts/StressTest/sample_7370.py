average_marks_premise = 55
average_marks_hypothesis = 35

# the hypothesis talks about the average marks of Suresh in English and History, which is also mentioned in the premise
if average_marks_hypothesis!= average_marks_premise:
    # check if the average marks in the hypothesis contradicts the average marks reported in the premise
    label = "contradiction"
else:
    # if the average marks in the hypothesis does not contradict the average marks in the premise, we can infer entailment
    label = "entailment"

print(label)
