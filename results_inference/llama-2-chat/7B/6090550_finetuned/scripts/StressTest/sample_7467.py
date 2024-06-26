level_premise = 1
level_hypothesis = 7
percentage_premise = 0.1
percentage_hypothesis = 0.1

# the hypothesis refers to the level of college graduates mentioned in the premise
if level_premise >= level_hypothesis:
    # check if the level in the hypothesis contradicts the level in the premise
    label = "contradiction"
elif percentage_hypothesis!= percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
