# Premise: At the faculty of Aerospace Engineering, less than 812 students study Random-processing methods, 222 students study Scramjet rocket engines and 112 students study them both.
# Hypothesis: At the faculty of Aerospace Engineering, 312 students study Random-processing methods, 222 students study Scramjet rocket engines and 112 students study them both.
# Golden Label: neutral

students_random_processing_premise = 812
students_random_processing_hypothesis = 312
students_scramjet_premise = 222
students_scramjet_hypothesis = 222
students_both_premise = 112
students_both_hypothesis = 112

# the hypothesis refers to the number of students studying different subjects mentioned in the premise
if students_random_processing_hypothesis >= students_random_processing_premise:
    # check if the number of students studying Random-processing methods in the hypothesis contradicts the premise
    label = "contradiction"
elif students_scramjet_hypothesis != students_scramjet_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the premise
    label = "contradiction"
elif students_both_hypothesis != students_both_premise:
    # check if the number of students studying both subjects in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

