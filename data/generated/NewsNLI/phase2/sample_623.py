# Premise: The attack killed four Somali civilians and 17 Ugandan and Burundian soldiers, including the mission's second in command, Burundian Maj. Gen. Juvenal Niyonguruza, he said.
# Hypothesis: Seventeen soldiers, four civilians killed in attack on African Union base.
# Golden Label: neutral

civilians_premise = 4
civilians_hypothesis = 4
soldiers_premise = 17
soldiers_hypothesis = 17

# the hypothesis mentions the number of civilians and soldiers killed in the attack, which is also referenced in the premise
if civilians_hypothesis != civilians_premise:
    # check if the number of civilians in the hypothesis contradicts the number of civilians reported in the premise
    label = "contradiction"
elif soldiers_hypothesis != soldiers_premise:
    # check if the number of soldiers from the hypothesis contradicts the number of soldiers in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

