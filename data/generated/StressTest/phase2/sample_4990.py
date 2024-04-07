# Premise: The next day, Cara took the test, and with this grade included, the new average was more than 47.
# Hypothesis: The next day, Cara took the test, and with this grade included, the new average was 77.
# Golden Label: neutral

average_grade_premise = 47
average_grade_hypothesis = 77

# the hypothesis refers to the average grade mentioned in the premise
if average_grade_hypothesis <= average_grade_premise:
    # check if the average grade in the hypothesis contradicts the premise of having more than 'average_grade_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average grade
    # any average grade greater than 'average_grade_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

