# Premise: The average marks scored by Ganesh in English, Science, Mathematics and History is less than 15 from that scored by him in English, History, Geography and Mathematics.
# Hypothesis: The average marks scored by Ganesh in English, Science, Mathematics and History is less than more than 15 from that scored by him in English, History, Geography and Mathematics.
# Golden Label: contradiction

average_marks_scored_subjects1_premise = 15
average_marks_scored_subjects2_premise = 15
average_marks_scored_subjects1_hypothesis = 15
average_marks_scored_subjects2_hypothesis = 15

# the hypothesis talks about the average marks scored by Ganesh in two sets of subjects
# mentioned also in the premise
if not (average_marks_scored_subjects1_hypothesis == average_marks_scored_subjects1_premise and 
        average_marks_scored_subjects2_hypothesis == average_marks_scored_subjects2_premise):
    # check if the hypothesis values contradict the values from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

