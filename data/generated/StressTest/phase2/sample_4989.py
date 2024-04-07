# Premise: The next day, Cara took the test, and with this grade included, the new average was 77.
# Hypothesis: The next day, Cara took the test, and with this grade included, the new average was more than 47.
# Golden Label: entailment

average_grade_premise = 77
average_grade_hypothesis = 47

# the hypothesis refers to the average grade mentioned in the premise
if average_grade_premise <= average_grade_hypothesis:
    # check if the estimate of 'average_grade_hypothesis' contradicts the average grade in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

