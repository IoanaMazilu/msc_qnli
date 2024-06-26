random_processing_premise = 312
random_processing_hypothesis = 212
scramjet_engines_premise = 234
scramjet_engines_hypothesis = 234
both_studies_premise = 112
both_studies_hypothesis = 112

# the hypothesis refers to the number of students studying different subjects at the faculty of Aerospace Engineering
if random_processing_hypothesis!= random_processing_premise:
    # check if the number of students studying Random-processing methods in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif scramjet_engines_hypothesis!= scramjet_engines_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif both_studies_hypothesis!= both_studies_premise:
    # check if the number of students studying both subjects in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
