# Premise: The average marks scored by Ganesh in English, Science, Mathematics and History is less than 14 from that scored by him in English, History, Geography and Mathematics.
# Hypothesis: The average marks scored by Ganesh in English, Science, Mathematics and History is less than less than 24 from that scored by him in English, History, Geography and Mathematics.
# Golden Label: entailment

average_marks_premise = 14
average_marks_hypothesis = 24

# the hypothesis refers to the average marks difference mentioned in the premise
if average_marks_premise >= average_marks_hypothesis:
    # check if the estimate of 'average_marks_hypothesis' contradicts the number of average marks difference in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

