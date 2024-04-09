random_processing_premise = 302
random_processing_hypothesis = 102
scramjet_premise = 232
scramjet_hypothesis = 232
both_premise = 112
both_hypothesis = 112

# the hypothesis refers to the number of students studying different subjects at the faculty of Aerospace Engineering, as mentioned in the premise
if random_processing_hypothesis!= random_processing_premise:
    # check if the number of students studying Random-processing methods in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif scramjet_hypothesis!= scramjet_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif both_hypothesis!= both_premise:
    # check if the number of students studying both subjects in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
