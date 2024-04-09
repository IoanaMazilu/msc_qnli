people_killed_premise = 70000
people_killed_hypothesis = 200000

# the hypothesis talks about the number of people killed in an air attack in the Darfur region, which is not referenced in the premise (the type of attack is not mentioned)
# the hypothesis cannot be entailed from the premise, since the number of people killed in the air attack is unknown.
label = "neutral"

print(label)
