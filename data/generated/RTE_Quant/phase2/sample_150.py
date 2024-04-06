# Premise: Stolen Warhol works recovered:Amsterdam police said Wednesday that they have recovered stolen lithographs by the late U.S. pop artist Andy Warhol worth more than $1 million. Dali's paintings are still missing.
# Hypothesis: Millions of dollars of art were recovered, including works by Dali.
# Golden Label: neutral

recovered_art_value_premise = 1e6
recovered_artist_premise = "Warhol"
missing_artist_premise = "Dali"

# the hypothesis implies that both Warhol and Dali's works were recovered
# but the premise explicitly mentions that Dali's paintings are still missing
# this indicates a contradiction between the premise and the hypothesis

if missing_artist_premise in ["Warhol", "Dali"]:
    label = "contradiction"
else:
    label = "neutral"

print(label)

