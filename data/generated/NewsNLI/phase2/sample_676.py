# Premise: (CNN) -- An alleged would-be smuggler was caught at a Thailand airport with dozens of rare wildlife -- including snakes, squirrels and tortoises -- stuffed into three suitcases, a wildlife monitoring organization says.
# Hypothesis: He had three suitcases stuffed with rare creatures, Traffic says.
# Golden Label: neutral

suitcases_premise = 3
suitcases_hypothesis = 3

# the hypothesis mentions the number of suitcases with rare creatures, which is also referenced in the premise
# however, the hypothesis does not specify the types of creatures, which is mentioned in the premise
# hence, we cannot confirm whether the creatures in the hypothesis are exactly the same as in the premise
label = "neutral"

print(label)

