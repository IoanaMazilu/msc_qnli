# Premise: The average marks scored by Ganesh in English, Science, Mathematics and History is less than 16 from that scored by him in English, History, Geography and Mathematics.
# Hypothesis: The average marks scored by Ganesh in English, Science, Mathematics and History is less than 86 from that scored by him in English, History, Geography and Mathematics.
# Golden Label: contradiction

average_marks_diff_premise = 16
average_marks_diff_hypothesis = 86

# The hypothesis refers to the difference in average marks scored by Ganesh in different subjects mentioned in the premise

if average_marks_diff_hypothesis < average_marks_diff_premise:
    # check if the difference in average marks in the hypothesis contradicts the difference mentioned in the premise
    label = "contradiction"
elif average_marks_diff_hypothesis == average_marks_diff_premise:
    # check if the difference in average marks in the hypothesis is the same as the difference mentioned in the premise
    label = "entailment"
else:
    # if the difference in average marks in the hypothesis does not contradict the difference mentioned in the premise and is not the same, we can infer neutrality
    label = "neutral"

print(label)

