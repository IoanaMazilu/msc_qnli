chance_of_death_premise = 500
chance_of_death_hypothesis = 5

# the hypothesis mentions the increased chance of death for women in domestic abuse situations if the abuser has access to a gun
# the premise also mentions this, but provides a specific percentage
# we can't infer from the premise that the chance of death is five times higher than stated in the hypothesis
if chance_of_death_hypothesis > chance_of_death_premise:
    # check if the chance of death in the hypothesis contradicts the chance of death reported in the premise
    label = "contradiction"
else:
    # if the chance of death in the hypothesis does not contradict the chance of death in the premise, we can infer neutrality
    label = "neutral"

print(label)
