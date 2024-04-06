# Premise: One of seven people killed in an explosion at a busy shopping centre near Helsinki was suspected to have carried out the attack, police have said.
# Hypothesis: The teenage bomber behind a blast was one of the seven people who died.
# Golden Label: neutral

people_killed_premise = 7
people_killed_hypothesis = 7
suspect_premise = 1
suspect_hypothesis = 1

# the hypothesis talks about the number of people killed and the suspect which are also mentioned in the premise
# the premise does not specify the age of the suspect, so we cannot infer if the suspect was a teenager
# hence, we cannot infer entailment or contradiction, so the relation is neutral

label = "neutral"

print(label)

