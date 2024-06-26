student_ranking_premise = 75
student_ranking_hypothesis = 15

# the hypothesis talks about the ranking of a student in a class, referenced also in the premise
if student_ranking_hypothesis >= student_ranking_premise:
    # check if the hypothesis value contradicts the estimate of less than'student_ranking_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ranking of the student
    # any ranking greater than'student_ranking_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
