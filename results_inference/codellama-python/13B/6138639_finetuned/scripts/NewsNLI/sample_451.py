killed_by_law_enforcement_premise = 48
killed_by_law_enforcement_hypothesis = 48
killed_by_other_animals_premise = 2
killed_by_other_animals_hypothesis = 2

# the hypothesis mentions the number of animals killed by law enforcement and the number of primates killed by the other animals, which are also mentioned in the premise
if killed_by_law_enforcement_hypothesis!= killed_by_law_enforcement_premise:
    # check if the number of animals killed by law enforcement in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif killed_by_other_animals_hypothesis!= killed_by_other_animals_premise:
    # check if the number of primates killed by the other animals from the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
