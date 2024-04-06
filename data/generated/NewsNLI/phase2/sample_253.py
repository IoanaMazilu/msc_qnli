# Premise: In domestic abuse situations, if the abuser has access to a gun, it increases the chance that a woman will die by 500%.
# Hypothesis: In domestic abuse situations, women five times more likely to die if abuser has access to gun.
# Golden Label: entailment

chance_increase_premise = 500
chance_increase_hypothesis = 5

# the hypothesis mentions the increase in the chance of a woman dying in domestic abuse situations if the abuser has access to a gun, which is also referenced in the premise
# it's important to note that the premise describes the increase as a percentage, while the hypothesis describes it as a multiplication factor
if chance_increase_hypothesis * 100 != chance_increase_premise:
    # check if the increase in the chance of death from the hypothesis contradicts the increase in the chance of death reported in the premise
    label = "contradiction"
else:
    # if the increase in the chance of death in the hypothesis does not contradict the increase in the chance of death in the premise, we can infer entailment
    label = "entailment"

print(label)

