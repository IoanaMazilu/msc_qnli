# Premise: Spokesmen for two groups linked to the Pakistani Taliban -- Jundallah and Jamaat-ul-Ahrar -- separately claimed responsibility for the bombing, with the spokesman for the latter, Ehsanullah Ehsan, calling the Jundallah claim'' baseless.''
# Hypothesis: Two groups claim responsibility for bombing, and one promises more attacks.
# Golden Label: neutral

groups_premise = 2
groups_hypothesis = 2

# the hypothesis mentions the number of groups claiming responsibility for the bombing, which is also mentioned in the premise
# however, the hypothesis refers to a promise of more attacks, which cannot be entailed from the premise
label = "neutral"

print(label)

