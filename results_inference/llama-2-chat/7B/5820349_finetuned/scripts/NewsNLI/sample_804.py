bombs_premise = 2
bombs_hypothesis = 2

# the hypothesis mentions the number of bombs in Karbala and Baghdad, which are also referenced in the premise
# however, the hypothesis refers to a different location (Baghdad) than the premise (Karbala)
# we cannot infer the number of bombs in Baghdad from the premise, so the relation is neutral
label = "neutral"

print(label)
