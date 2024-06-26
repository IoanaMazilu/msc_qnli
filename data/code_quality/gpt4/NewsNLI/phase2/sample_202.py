hells_angels_dead_premise = 1
hells_angels_dead_hypothesis = 1
vagos_injured_premise = 2
vagos_injured_hypothesis = 2

# the hypothesis mentions the number of Hell's Angels members who died and the Vagos members who are injured, which are also mentioned in the premise
if hells_angels_dead_hypothesis != hells_angels_dead_premise:
    # check if the number of Hell's Angels members who died in the hypothesis contradicts the same number in the premise
    label = "contradiction"
elif vagos_injured_hypothesis != vagos_injured_premise:
    # check if the number of Vagos members who are injured in the hypothesis contradicts the same number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
