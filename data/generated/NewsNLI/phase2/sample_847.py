# Premise: Three police officials and two civilians were killed in the explosion, said Imran Shahid, the police officer.
# Hypothesis: The attack wounds 31 people, a police officer on the scene says.
# Golden Label: neutral

police_officials_killed_premise = 3
civilians_killed_premise = 2
people_wounded_hypothesis = 31

# the premise mentions the number of police officials and civilians killed in an explosion
# the hypothesis mentions the number of people wounded in an attack
# there is no direct correlation or contradiction between people being killed and people being wounded in these contexts
# therefore, no comparison is needed here
label = "neutral"

print(label)

