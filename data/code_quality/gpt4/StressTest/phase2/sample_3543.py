apple_code_premise = 0
apple_code_hypothesis = 6
flower_code_premise = 63
flower_code_hypothesis = 63

# the hypothesis talks about certain codes for APPLE and FLOWER referenced also in the premise
if apple_code_premise >= apple_code_hypothesis:
    # check if the hypothesis value contradicts the code of APPLE in the premise
    label = "contradiction"
elif flower_code_hypothesis != flower_code_premise:
    # check if the code of FLOWER in the hypothesis contradicts the code of FLOWER in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
