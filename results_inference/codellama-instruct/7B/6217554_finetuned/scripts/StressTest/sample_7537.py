obtained_premise = [50, 60, 70, 80, 80]
obtained_hypothesis = [40, 60, 70, 80, 80]
total_marks_premise = 100
total_marks_hypothesis = 100

# the hypothesis talks about the obtained marks in different subjects, referenced also in the premise
if obtained_hypothesis!= obtained_premise:
    # check if the obtained marks in the hypothesis contradict the obtained marks reported in the premise
    label = "contradiction"
elif total_marks_hypothesis!= total_marks_premise:
    # check if the total marks in the hypothesis contradict the total marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
