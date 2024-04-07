# Premise: 90 students represent x percent of the boys at Jones Elementary School.
# Hypothesis: more than 90 students represent x percent of the boys at Jones Elementary School.
# Golden Label: contradiction

students_premise = 90
students_hypothesis = 90

# the hypothesis talks about the number of students, referenced also in the premise
if students_hypothesis >= students_premise:
    # check if the hypothesis value contradicts the exact number of 'students_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of students
    # any number of students less than 'students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)

