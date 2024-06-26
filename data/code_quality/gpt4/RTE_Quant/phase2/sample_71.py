apollo_16_astronauts_premise = 2
apollo_16_astronauts_hypothesis = 16

# the hypothesis talks about the number of astronauts that have been to the moon, which contradicts with the premise (only 2 astronauts from Apollo 16 have been to the moon according to the premise)
if apollo_16_astronauts_premise < apollo_16_astronauts_hypothesis:
    label = "contradiction"
else:
    label = "entailment"

print(label)
