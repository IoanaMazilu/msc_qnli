# Premise: The earthquake is blamed for killing more than 212,000 people, injuring 300,000 and leaving more than 1 million homeless in the city of 3 million and surrounding communities.
# Hypothesis: Quake killed more than 212,000 people, left more than 1 million homeless in city, nearby.
# Golden Label: entailment

dead_premise = 212000 
homeless_premise = 1000000 
dead_hypothesis = 212000 
homeless_hypothesis = 1000000 

# the hypothesis mentions the number of dead and homeless people, which is also mentioned in the premise
# the hypothesis does not provide any information about injured people which is given in the premise
# hence, we cannot infer entailment or contradiction based on this information
if dead_hypothesis != dead_premise:
    # check if the number of dead people in the hypothesis contradicts the number of dead people reported in the premise
    label = "contradiction"
elif homeless_hypothesis != homeless_premise:
    # check if the number of homeless people from the hypothesis contradicts the number of homeless people in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutral as the hypothesis does not consider all the information from the premise
    label = "neutral"

print(label)

