# Premise: The average marks scored by Ganesh in English, Science, Mathematics and History is less than 20 from that scored by him in English, History, Geography and Mathematics.
# Hypothesis: The average marks scored by Ganesh in English, Science, Mathematics and History is less than 30 from that scored by him in English, History, Geography and Mathematics.
# Golden Label: contradiction

average_marks_premise = 20
average_marks_hypothesis = 30

# the hypothesis talks about the difference in average marks scored by Ganesh in multiple subjects, referenced also in the premise
if average_marks_hypothesis < average_marks_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'average_marks_premise'
    label = "contradiction"
elif average_marks_hypothesis == average_marks_premise:
    # check if the hypothesis value is exactly the same as the premise value
    label = "entailment"
else:
    # the premise gives only an estimate for the difference in average marks
    # any difference greater than 'average_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

