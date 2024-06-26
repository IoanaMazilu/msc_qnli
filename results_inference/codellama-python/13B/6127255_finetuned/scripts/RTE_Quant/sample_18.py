total_killed_premise = 70000
total_displaced_premise = 2000000
air_attack_killed_hypothesis = 200000

# the hypothesis talks about the number of people killed in an air attack, which is not mentioned in the premise
# the premise only mentions the total number of people killed and displaced in the Darfur region
# the hypothesis cannot be entailed from the premise, since the number of people killed in the air attack is unknown.
label = "neutral"

print(label)
