mortar_attack_premise = 4
killed_premise = 80
kidnapped_premise = 1

# the hypothesis talks about the number of guardsmen killed and injured, which is also mentioned in the premise
if killed_hypothesis!= killed_premise or injured_hypothesis!= injured_premise:
    # check if the number of guardsmen killed and injured in the hypothesis contradicts the number of guardsmen killed and injured in the premise
    label = "contradiction"
elif kidnapped_hypothesis!= kidnapped_premise:
    # check if the kidnapping of a top official from a prominent charity in the hypothesis contradicts the information in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
