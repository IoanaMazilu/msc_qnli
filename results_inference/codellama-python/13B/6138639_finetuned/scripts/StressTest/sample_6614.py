random_processing_students_premise = 312
random_processing_students_hypothesis = 212
scramjet_rocket_engine_students_premise = 234
scramjet_rocket_engine_students_hypothesis = 234
both_students_premise = 112
both_students_hypothesis = 112

# the hypothesis refers to the number of students studying each subject at the faculty of Aerospace Engineering, mentioned in the premise
if random_processing_students_premise!= random_processing_students_hypothesis:
    # check if the number of students studying Random-processing methods in the hypothesis contradicts the number of students in the premise
    label = "contradiction"
elif scramjet_rocket_engine_students_premise!= scramjet_rocket_engine_students_hypothesis:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students in the premise
    label = "contradiction"
elif both_students_premise!= both_students_hypothesis:
    # check if the number of students studying both subjects in the hypothesis contradicts the number of students in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
