official_premise = "one Secret Service agent was found intoxicated and passed out in the hallway of his hotel"
official_hypothesis = "one of them was found drunk in a hotel hallway"

# the hypothesis mentions the number of Secret Service agents found drunk, which is not mentioned in the premise
# therefore, we cannot infer entailment or contradiction from this information
label = "neutral"

print(label)
