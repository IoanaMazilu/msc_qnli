# Premise: At the faculty of Aerospace Engineering, 312 students study Random-processing methods, 234 students study Scramjet rocket engines and 112 students study them both.
# Hypothesis: At the faculty of Aerospace Engineering, 212 students study Random-processing methods, 234 students study Scramjet rocket engines and 112 students study them both.
# Golden Label: contradiction

random_processing_premise = 312
random_processing_hypothesis = 212
scramjet_rocket_premise = 234
scramjet_rocket_hypothesis = 234
both_premise = 112
both_hypothesis = 112

# the hypothesis refers to the number of students studying different subjects at the faculty of Aerospace Engineering
if random_processing_premise != random_processing_hypothesis:
    # check if the number of students studying Random-processing methods in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif scramjet_rocket_premise != scramjet_rocket_hypothesis:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif both_premise != both_hypothesis:
    # check if the number of students studying both subjects in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

