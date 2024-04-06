# Premise: One Hell's Angels member died from his wounds, while two associated with Vagos suffered what the deputy chief described as'' non-life-threatening'' injuries.
# Hypothesis: 1 Hell's Angels member has died, 2 Vagos members have'' non-life-threatening'' injuries.
# Golden Label: entailment

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

