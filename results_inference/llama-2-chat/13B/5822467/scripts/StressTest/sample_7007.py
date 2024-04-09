gerbil_premise = 96
hamster_premise = 96
gerbil_hypothesis = 66
hamster_hypothesis = 66

# the hypothesis refers to the total number of pets, which is the sum of gerbils and hamsters
if gerbil_premise + hamster_premise == gerbil_hypothesis + hamster_hypothesis:
    # check if the hypothesis value is consistent with the premise value
    label = "neutral"
elif gerbil_premise < gerbil_hypothesis or hamster_premise < hamster_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
