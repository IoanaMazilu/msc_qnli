passengers_premise = 14
passengers_hypothesis = 14
attendants_premise = 2
attendants_hypothesis = 2

# the hypothesis mentions the number of passengers and flight attendants that were injured, which are also mentioned in the premise
if passengers_hypothesis != passengers_premise:
    # check if the number of injured passengers in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif attendants_hypothesis != attendants_premise:
    # check if the number of injured flight attendants from the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
