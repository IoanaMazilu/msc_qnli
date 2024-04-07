# Premise: The next day, Ella took the test, and with this grade included, the new average was less than 85.
# Hypothesis: The next day, Ella took the test, and with this grade included, the new average was 75.
# Golden Label: neutral

average_premise = 85
average_hypothesis = 75

# the hypothesis refers to the same context as the premise, which is Ella's new average grade after taking a test
if average_hypothesis >= average_premise:
    # check if the hypothesis value contradicts the premise's indication of an average grade less than 'average_premise'
    label = "contradiction"
else:
    # the premise gives only an upper limit for the average grade
    # any average grade less than 'average_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

