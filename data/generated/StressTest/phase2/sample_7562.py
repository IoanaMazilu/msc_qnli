# Premise: At the faculty of Aerospace Engineering, 310 students study Random-processing methods, 232 students study Scramjet rocket engines and 112 students study them both.
# Hypothesis: At the faculty of Aerospace Engineering, 810 students study Random-processing methods, 232 students study Scramjet rocket engines and 112 students study them both.
# Golden Label: contradiction

random_processing_premise = 310
random_processing_hypothesis = 810
scramjet_engines_premise = 232
scramjet_engines_hypothesis = 232
both_subjects_premise = 112
both_subjects_hypothesis = 112

# the hypothesis refers to the number of students studying each subject and both subjects, as mentioned in the premise
if random_processing_hypothesis != random_processing_premise:
    # check if the number of students studying 'random-processing methods' in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif scramjet_engines_hypothesis != scramjet_engines_premise:
    # check if the number of students studying 'scramjet rocket engines' in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif both_subjects_hypothesis != both_subjects_premise:
    # check if the number of students studying both subjects in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

