total_students_premise = 20
total_students_hypothesis = 20

# the hypothesis talks about the number of students in the class, referenced also in the premise
if total_students_hypothesis!= total_students_premise:
    # check if the number of students in the hypothesis contradicts the number of students in the premise
    label = "contradiction"
else:
    # the premise gives an exact number for the number of students in the class
    # the hypothesis can be explicitly entailed from the premise
    label = "entailment"

print(label)
