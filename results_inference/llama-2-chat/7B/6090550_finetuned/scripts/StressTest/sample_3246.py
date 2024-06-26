students_premise = 90
students_hypothesis = 50
percentage = 0.x

# the hypothesis refers to the number of students representing x percent of the boys at Jones Elementary School
if students_premise <= students_hypothesis:
    # check if the number of students in the hypothesis contradicts the number of students in the premise
    label = "contradiction"
else:
    # if the number of students in the hypothesis is greater than the number of students in the premise, it does not contradict the premise
    label = "neutral"

print(label)
