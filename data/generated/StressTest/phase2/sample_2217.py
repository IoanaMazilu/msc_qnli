# Premise: In a friendship gang Andrew has 8 gang, in how many ways can he invite one or more of the gang to his house?
# Hypothesis: In a friendship gang Andrew has more than 1 gang, in how many ways can he invite one or more of the gang to his house?
# Golden Label: entailment

gang_count_premise = 8
gang_count_hypothesis = 1

# the hypothesis refers to the number of gangs that Andrew has, which is also mentioned in the premise
if gang_count_premise <= gang_count_hypothesis:
    # check if the number of gangs in the hypothesis contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

