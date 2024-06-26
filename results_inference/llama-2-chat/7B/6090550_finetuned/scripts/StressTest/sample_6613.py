random_processing_students_premise = 112
random_processing_students_hypothesis = 312
scramjet_rocket_engine_students_premise = 234
scramjet_rocket_engine_students_hypothesis = 234
both_students_premise = 112
both_students_hypothesis = 112

# the hypothesis talks about the number of students studying different topics, which are also mentioned in the premise
if random_processing_students_hypothesis!= random_processing_students_premise:
    label = "contradiction"
elif scramjet_rocket_engine_students_hypothesis!= scramjet_rocket_engine_students_premise:
    label = "contradiction"
elif both_students_hypothesis!= both_students_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
