students_premise = 700
students_hypothesis = 200

# the hypothesis talks about the number of grades higher than Lena's in another class
if students_hypothesis <= students_premise:
    # check if the hypothesis value contradicts the estimate of less than'students_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of grades
    # any number of grades greater than'students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
