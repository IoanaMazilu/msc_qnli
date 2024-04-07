# Premise: The average marks scored by Ganesh in English, Science, Mathematics and History is less than 16 from that scored by him in English, History, Geography and Mathematics.
# Hypothesis: The average marks scored by Ganesh in English, Science, Mathematics and History is less than less than 46 from that scored by him in English, History, Geography and Mathematics.
# Golden Label: entailment

avg_marks_premise = 16
avg_marks_hypothesis = 46

# The hypothesis talks about the average marks scored by Ganesh in certain subjects, referenced also in the premise
if avg_marks_hypothesis < avg_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'avg_marks_premise'
    label = "contradiction"
elif avg_marks_hypothesis == avg_marks_premise:
    # check if the hypothesis value is equal to the estimate of 'avg_marks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average marks
    # any average marks greater than 'avg_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

