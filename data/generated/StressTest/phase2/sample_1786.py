# Premise: The average marks scored by Ganesh in English, Science, Mathematics and History is less than less than 88 from that scored by him in English, History, Geography and Mathematics.
# Hypothesis: The average marks scored by Ganesh in English, Science, Mathematics and History is less than 18 from that scored by him in English, History, Geography and Mathematics.
# Golden Label: neutral

average_marks_premise = 88
average_marks_hypothesis = 18

# the hypothesis refers to the difference in average marks mentioned in the premise
if average_marks_hypothesis >= average_marks_premise:
    # check if the 'average_marks_hypothesis' contradicts the premise of less than 'average_marks_premise'
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, it can be inferred as an entailment
    label = "entailment"

print(label)

