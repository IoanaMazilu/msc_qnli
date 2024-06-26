reema_marks_premise = 85
reema_marks_hypothesis = 70

# define variables for the numerical entities in the premise and hypothesis
marks_premise = 50
average_marks_premise = marks_premise / 2
average_marks_hypothesis = reema_marks_hypothesis / 2

# compare the variables to determine the label
if marks_premise <= reema_marks_hypothesis:
    # check if the estimate of'reema_marks_hypothesis' contradicts the mark secured by Reema in the premise
    label = "contradiction"
elif marks_premise!= average_marks_premise or reema_marks_hypothesis!= average_marks_hypothesis:
    # check if the marks in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
