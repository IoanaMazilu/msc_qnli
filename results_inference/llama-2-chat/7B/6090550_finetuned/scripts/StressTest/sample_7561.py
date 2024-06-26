random_processing_students_premise = 110
scramjet_rocket_engine_students_premise = 232
joint_students_premise = 112

random_processing_students_hypothesis = 310
scramjet_rocket_engine_students_hypothesis = 232
joint_students_hypothesis = 112

# the hypothesis refers to the number of students studying different subjects, which are also mentioned in the premise
if random_processing_students_hypothesis!= random_processing_students_premise:
    label = "contradiction"
elif scramjet_rocket_engine_students_hypothesis!= scramjet_rocket_engine_students_premise:
    label = "contradiction"
elif joint_students_hypothesis!= joint_students_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
