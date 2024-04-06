# Premise: In Najaf, at least one person was killed and 10 were wounded in a bombing, the ministry said.
# Hypothesis: A car bomb in another Baghdad neighborhood kills at least one person.
# Golden Label: neutral

killed_premise = 1
killed_hypothesis = 1

# the hypothesis mentions at least one person killed by a car bomb, which is also mentioned in the premise
# however, the location of the bombing in the hypothesis (Baghdad neighborhood) cannot be entailed from the premise (Najaf)
# hence, we cannot infer entailment or contradiction based on the information given in the premise and the hypothesis
label = "neutral"

print(label)

