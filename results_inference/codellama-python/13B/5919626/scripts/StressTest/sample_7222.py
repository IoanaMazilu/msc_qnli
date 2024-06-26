students_premise = 700
students_hypothesis = 200
grades_higher_premise = 24
grades_higher_hypothesis = 24

# the hypothesis refers to the same class as the premise
if students_hypothesis >= students_premise:
    # check if the hypothesis value contradicts the estimate of less than'students_premise'
    label = "contradiction"
elif grades_higher_hypothesis!= grades_higher_premise:
    # check if the number of grades higher than Lena's in the hypothesis contradicts the number of grades higher than Lena's in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students
    # any number of students less than'students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)