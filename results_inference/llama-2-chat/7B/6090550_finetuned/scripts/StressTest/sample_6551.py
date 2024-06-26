birds_speed_premise = [4, 1]
birds_speed_hypothesis = [3, 1]

# the hypothesis refers to the speeds of the two birds flying towards each other, which are also mentioned in the premise
if birds_speed_hypothesis[0]!= birds_speed_premise[0]:
    # check if the speed of the first bird in the hypothesis contradicts the speed of the first bird in the premise
    label = "contradiction"
elif birds_speed_hypothesis[1]!= birds_speed_premise[1]:
    # check if the speed of the second bird in the hypothesis contradicts the speed of the second bird in the premise
    label = "contradiction"
else:
    # if the speeds in the hypothesis do not contradict the speeds in the premise, we can infer entailment
    label = "entailment"

print(label)
