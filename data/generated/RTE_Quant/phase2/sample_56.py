# Premise: Two persons were injured in dynamite attacks perpetrated this evening against two bank branches in this Northwestern Colombian city.
# Hypothesis: Two persons perpetrated dynamite attacks in a Northwestern Colombian city.
# Golden Label: neutral

persons_injured_premise = 2
persons_perpetrated_hypothesis = 2

# the hypothesis talks about the number of persons who perpetrated the attacks which is not mentioned in the premise
# the hypothesis cannot be entailed from the premise, since the number of persons who perpetrated the attacks is unknown.
label = "neutral"

print(label)

