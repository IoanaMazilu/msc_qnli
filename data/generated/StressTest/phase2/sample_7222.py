# Premise: In another class of less than 700 students there were 24 grades higher than Lena’s.
# Hypothesis: In another class of 200 students there were 24 grades higher than Lena’s.
# Golden Label: neutral

students_premise = 700
students_hypothesis = 200
grades_higher_than_lena = 24

# the hypothesis refers to the number of students and grades higher than Lena's mentioned in the premise
if students_premise <= students_hypothesis:
    # check if the number of students in the hypothesis contradicts the estimate of less than 'students_premise'
    label = "contradiction"
elif grades_higher_than_lena != grades_higher_than_lena:
    # check if the number of grades higher than Lena's in the hypothesis contradicts the number of grades higher than Lena's in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students
    # any number of students less than 'students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

