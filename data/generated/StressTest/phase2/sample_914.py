# Premise: The average marks scored by Ganesh in English, Science, Mathematics and History is less than 14 from that scored by him in English, History, Geography and Mathematics.
# Hypothesis: The average marks scored by Ganesh in English, Science, Mathematics and History is less than more than 14 from that scored by him in English, History, Geography and Mathematics.
# Golden Label: contradiction

avg_marks_premise = 14
avg_marks_hypothesis = 14

# the hypothesis refers to the difference in average marks mentioned in the premise
if avg_marks_hypothesis > avg_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'avg_marks_premise'
    label = "contradiction"
elif avg_marks_hypothesis < avg_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'avg_marks_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

