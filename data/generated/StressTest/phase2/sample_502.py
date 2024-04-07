# Premise: The average marks scored by Ganesh in English, Science, Mathematics and History is less than less than 46 from that scored by him in English, History, Geography and Mathematics.
# Hypothesis: The average marks scored by Ganesh in English, Science, Mathematics and History is less than 16 from that scored by him in English, History, Geography and Mathematics.
# Golden Label: neutral

average_marks_premise = 46
average_marks_hypothesis = 16

# the hypothesis refers to the average marks difference between two sets of subjects, also mentioned in the premise
if average_marks_hypothesis >= average_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_marks_premise'
    label = "contradiction"
elif average_marks_hypothesis < average_marks_premise:
    # check if the value in the hypothesis is less than the value in the premise
    label = "entailment"
else:
    # if the hypothesis value matches exactly with the premise, it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

