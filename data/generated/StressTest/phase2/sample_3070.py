# Premise: more than 60 students represent x percent of the boys at Jones Elementary School.
# Hypothesis: 90 students represent x percent of the boys at Jones Elementary School.
# Golden Label: neutral

students_represent_premise = 60
students_represent_hypothesis = 90

# the hypothesis talks about the number of students representing a certain percent of boys, referenced also in the premise
if students_represent_hypothesis <= students_represent_premise:
    # check if the number of students in the hypothesis contradicts the estimate of more than 'students_represent_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students
    # any number of students greater than 'students_represent_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

