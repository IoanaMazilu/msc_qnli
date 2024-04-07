# Premise: At the faculty of Aerospace Engineering, 312 students study Random-processing methods, 232 students study Scramjet rocket engines and 114 students study them both.
# Hypothesis: At the faculty of Aerospace Engineering, less than 412 students study Random-processing methods, 232 students study Scramjet rocket engines and 114 students study them both.
# Golden Label: entailment

random_processing_premise = 312
random_processing_hypothesis = 412
scramjet_premise = 232
scramjet_hypothesis = 232
both_premise = 114
both_hypothesis = 114

# the hypothesis refers to the number of students studying different subjects mentioned in the premise
if random_processing_hypothesis < random_processing_premise:
    # check if the estimate of 'random_processing_hypothesis' contradicts the number of students studying Random-processing methods in the premise
    label = "contradiction"
elif scramjet_hypothesis != scramjet_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of such students reported in the premise
    label = "contradiction"
elif both_hypothesis != both_premise:
    # check if the number of students studying both subjects in the hypothesis contradicts the number of such students reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

