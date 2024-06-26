premise_killed = 70000
premise_displaced = 2000000
hypothesis_killed = 200000

# the hypothesis talks about the number of people killed in an air attack, which is not mentioned in the premise
# the hypothesis cannot be entailed from the premise, since the number of people killed in the air attack is unknown.
label = "neutral"

print(label)
