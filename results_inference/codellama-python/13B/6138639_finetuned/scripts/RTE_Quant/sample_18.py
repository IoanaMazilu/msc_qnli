total_people_killed_premise = 70e3
total_people_killed_hypothesis = 200e3

# the hypothesis talks about the number of people killed in an air attack, which is not mentioned in the premise
# the hypothesis cannot be entailed from the premise, since the number of people killed in the air attack is unknown.
label = "neutral"

print(label)
