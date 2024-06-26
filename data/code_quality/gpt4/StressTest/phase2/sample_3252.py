random_processing_premise = 312
random_processing_hypothesis = 812
scramjet_engines_premise = 222
scramjet_engines_hypothesis = 222
both_studies_premise = 112
both_studies_hypothesis = 112

# the hypothesis refers to the number of students studying different subjects at the Faculty of Aerospace Engineering, mentioned in the premise
if random_processing_hypothesis <= random_processing_premise:
    # check if the estimate of 'random_processing_hypothesis' contradicts the number of students studying Random-processing methods in the premise
    label = "contradiction"
elif scramjet_engines_premise != scramjet_engines_hypothesis:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of such students reported in the premise
    label = "contradiction"
elif both_studies_premise != both_studies_hypothesis:
    # check if the number of students studying both subjects in the hypothesis contradicts the number of such students reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
