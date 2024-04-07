# Premise: more than 30 students represent x percent of the boys at Jones Elementary School.
# Hypothesis: 90 students represent x percent of the boys at Jones Elementary School.
# Golden Label: neutral

students_premise = 30
students_hypothesis = 90

# the hypothesis refers to the number of students mentioned in the premise
if students_hypothesis <= students_premise:
    # check if the hypothesis value contradicts the estimate of more than 'students_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students
    # any number of students greater than 'students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

