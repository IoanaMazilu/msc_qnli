random_processing_students_premise = 310
random_processing_students_hypothesis = 810
scramjet_rocket_engine_students_premise = 232
scramjet_rocket_engine_students_hypothesis = 232
both_students_premise = 112
both_students_hypothesis = 112

# the hypothesis talks about the number of students studying each subject, referenced also in the premise
if random_processing_students_hypothesis!= random_processing_students_premise:
    # check if the number of students studying Random-processing methods in the hypothesis contradicts the number of students in the premise
    label = "contradiction"
elif scramjet_rocket_engine_students_hypothesis!= scramjet_rocket_engine_students_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students in the premise
    label = "contradiction"
elif both_students_hypothesis!= both_students_premise:
    # check if the number of students studying both subjects in the hypothesis contradicts the number of students in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
