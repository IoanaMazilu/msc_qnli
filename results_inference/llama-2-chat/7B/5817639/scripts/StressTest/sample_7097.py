students_premise = 47
students_hypothesis = 65

# the hypothesis talks about the ranking of a student, referenced also in the premise
if students_hypothesis <= students_premise:
    # check if the hypothesis value contradicts the estimate of the ranking in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ranking
    # any ranking greater than'students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
