# Premise: The next day, Alice took the test, and with this grade included, the new average was more than 29.
# Hypothesis: The next day, Alice took the test, and with this grade included, the new average was 79.
# Golden Label: neutral

average_grade_premise = 29
average_grade_hypothesis = 79

# the hypothesis talks about Alice's average grade, referenced also in the premise
if average_grade_hypothesis <= average_grade_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_grade_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average grade
    # any average grade greater than 'average_grade_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

