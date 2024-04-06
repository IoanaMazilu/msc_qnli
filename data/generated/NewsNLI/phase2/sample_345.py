# Premise: Families of the 12 who died and five victims'' who suffered permanent brain damage or permanent physical paralysis, will each receive $220,000.
# Hypothesis: Families of the deceased and victims with debilitating damage will receive $220,000.
# Golden Label: entailment

death_victims_premise = 12
permanent_damage_victims_premise = 5
compensation_premise = 220000

# the hypothesis does not mention the number of death victims or the number of victims with permanent damage
# it also does not contradict the amount of compensation mentioned in the premise
# therefore, we can't infer entailment or contradiction based on the hypothesis
label = "neutral"

print(label)

