# Premise: The average marks scored by Ganesh in English, Science, Mathematics and History is less than 18 from that scored by him in English, History, Geography and Mathematics.
# Hypothesis: The average marks scored by Ganesh in English, Science, Mathematics and History is less than less than 88 from that scored by him in English, History, Geography and Mathematics.
# Golden Label: entailment

average_marks_premise = 18
average_marks_hypothesis = 88

# the hypothesis refers to the difference in average marks in the same subjects as the premise
if average_marks_hypothesis <= average_marks_premise:
    # check if the estimate of 'average_marks_hypothesis' contradicts the estimate of the difference in average marks in the premise
    label = "contradiction"
elif average_marks_hypothesis > average_marks_premise:
    # check if the estimate of 'average_marks_hypothesis' could be inferred from the estimate of the difference in average marks in the premise
    label = "entailment"

print(label)

