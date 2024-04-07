# Premise: At the faculty of Aerospace Engineering, 302 students study Random-processing methods, 232 students study Scramjet rocket engines and 112 students study them both.
# Hypothesis: At the faculty of Aerospace Engineering, more than 102 students study Random-processing methods, 232 students study Scramjet rocket engines and 112 students study them both.
# Golden Label: entailment

random_processing_premise = 302
scramjet_rocket_premise = 232
both_subjects_premise = 112

random_processing_hypothesis = 102
scramjet_rocket_hypothesis = 232
both_subjects_hypothesis = 112

# the hypothesis refers to the number of students that study each subject mentioned in the premise
if random_processing_hypothesis >= random_processing_premise:
    # check if the estimate of 'random_processing_hypothesis' contradicts the number of Random-processing students in the premise
    label = "contradiction"
elif scramjet_rocket_hypothesis != scramjet_rocket_premise:
    # check if the number of Scramjet rocket students in the hypothesis contradicts the number of Scramjet rocket students reported in the premise
    label = "contradiction"
elif both_subjects_hypothesis != both_subjects_premise:
    # check if the number of students studying both subjects in the hypothesis contradicts the number of students studying both subjects reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

