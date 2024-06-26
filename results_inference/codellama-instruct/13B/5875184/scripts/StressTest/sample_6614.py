faculty_students_premise = 312
faculty_students_hypothesis = 212
random_processing_premise = 312 - 234
random_processing_hypothesis = 212 - 234
scramjet_rocket_engines_premise = 234
scramjet_rocket_engines_hypothesis = 234
both_premise = 112
both_hypothesis = 112

# the hypothesis refers to the number of students studying Random-processing methods and Scramjet rocket engines
if random_processing_hypothesis <= random_processing_premise and scramjet_rocket_engines_hypothesis <= scramjet_rocket_engines_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif both_hypothesis!= both_premise:
    # check if the number of students studying both Random-processing methods and Scramjet rocket engines contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
