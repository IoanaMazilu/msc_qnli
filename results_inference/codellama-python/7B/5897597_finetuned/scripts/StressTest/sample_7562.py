random_processing_students_premise = 310
random_processing_students_hypothesis = 810
scramjet_students_premise = 232
scramjet_students_hypothesis = 232
both_students_premise = 112
both_students_hypothesis = 112

# the hypothesis refers to the number of students studying different subjects at the faculty of Aerospace Engineering, mentioned in the premise
if random_processing_students_premise!= random_processing_students_hypothesis:
    # check if the number of students studying Random-processing methods in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif scramjet_students_premise!= scramjet_students_hypothesis:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif both_students_premise!= both_students_hypothesis:
    # check if the number of students studying both subjects in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)