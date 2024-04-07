# Premise: In a friendship gang Aravind has 2 gang, in how many ways can he invite one or more of the gang to his house?
# Hypothesis: In a friendship gang Aravind has more than 1 gang, in how many ways can he invite one or more of the gang to his house?
# Golden Label: entailment

gang_premise = 2
gang_hypothesis = 1

# the hypothesis refers to the number of gangs that Aravind has, which was mentioned in the premise
if gang_premise <= gang_hypothesis:
    # check if the number of gangs in the hypothesis contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

