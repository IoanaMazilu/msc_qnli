marks_premise = [76, 65, 82, 67, 85]
marks_hypothesis = [46, 65, 82, 67, 85]

# the hypothesis talks about the marks obtained by Arun in 6 subjects
if any(marks_hypothesis <= marks_premise):
    # check if the hypothesis value contradicts any of the marks in the premise
    label = "contradiction"
else:
    # the premise gives a list of marks obtained by Arun, and the hypothesis values are consistent with those marks
    label = "entailment"

print(label)
