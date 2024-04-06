# Premise: Nevada Highway Patrol Trooper Danny Lopez said two people died in the accident:one person on the train and one in the semitrailer.
# Hypothesis: One person on the train and one in the truck died, authorities say.
# Golden Label: entailment

death_train_premise = 1
death_train_hypothesis = 1
death_semitrailer_premise = 1
death_truck_hypothesis = 1

# the hypothesis mentions the number of deaths on the train and in the truck, which are also mentioned in the premise
if death_train_hypothesis != death_train_premise:
    # check if the number of deaths on the train in the hypothesis contradicts the number of deaths on the train reported in the premise
    label = "contradiction"
elif death_truck_hypothesis != death_semitrailer_premise:
    # check if the number of deaths in the truck from the hypothesis contradicts the number of deaths in the semitrailer in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

