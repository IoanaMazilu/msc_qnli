grades_premise = 200
grades_hypothesis = 300

# the hypothesis refers to the number of grades higher than Lena's in another class
if grades_hypothesis >= grades_premise:
    # check if the estimate of 'grades_hypothesis' contradicts the number of grades in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of grades
    # any number of grades greater than 'grades_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
