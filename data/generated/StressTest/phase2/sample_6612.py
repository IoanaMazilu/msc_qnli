# Premise: At the faculty of Aerospace Engineering, 312 students study Random-processing methods, 234 students study Scramjet rocket engines and 112 students study them both.
# Hypothesis: At the faculty of Aerospace Engineering, more than 112 students study Random-processing methods, 234 students study Scramjet rocket engines and 112 students study them both.
# Golden Label: entailment

random_processing_students_premise = 312
scramjet_students_premise = 234
both_subjects_students_premise = 112

random_processing_students_hypothesis = 112
scramjet_students_hypothesis = 234
both_subjects_students_hypothesis = 112

# the hypothesis refers to the number of students studying each subject mentioned in the premise
if random_processing_students_hypothesis >= random_processing_students_premise:
    # check if the estimate of 'random_processing_students_hypothesis' contradicts the number of students studying Random-processing methods in the premise
    label = "contradiction"
elif scramjet_students_hypothesis != scramjet_students_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students studying Scramjet rocket engines reported in the premise
    label = "contradiction"
elif both_subjects_students_hypothesis != both_subjects_students_premise:
    # check if the number of students studying both subjects in the hypothesis contradicts the number of students studying both subjects reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

