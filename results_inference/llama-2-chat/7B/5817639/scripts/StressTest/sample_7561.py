random_processing_premise = 110
scramjet_rocket_engine_premise = 232
both_premise = 112

# the hypothesis talks about the number of students studying different topics at the faculty of Aerospace Engineering
if random_processing_hypothesis <= random_processing_premise:
    # check if the hypothesis value contradicts the estimate of more than 'random_processing_premise' students studying Random-processing methods
    label = "contradiction"
elif scramjet_rocket_engine_hypothesis!= scramjet_rocket_engine_premise:
    # check if the number of students studying Scramjet rocket engines in the hypothesis contradicts the number of students reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
