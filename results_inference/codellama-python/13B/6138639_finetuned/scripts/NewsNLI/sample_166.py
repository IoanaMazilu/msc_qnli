new_species_premise = 200
new_species_hypothesis = 200

# the hypothesis mentions the number of new species of amphibians found in Madagascar, which is also mentioned in the premise
if new_species_hypothesis!= new_species_premise:
    # check if the number of new species in the hypothesis contradicts the number of new species reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
