# Premise: Amsterdam police said Wednesday that they have recovered stolen lithographs by the late U.S. pop artist Andy Warhol worth more than $1 million.
# Hypothesis: Police recovered 81 Andy Warhol lithographs.
# Golden Label: neutral

artwork_value_premise = 1e6

# the hypothesis talks about the number of lithographs, which is not mentioned in the premise
# the hypothesis cannot be entailed from the premise, since the number of lithographs is unknown.
label = "neutral"

print(label)

