# Premise: Proctor was also ordered to pay about $58,000 in restitution to two women he knifed in the throat, prosecutors said.
# Hypothesis: Proctor also has to pay money to two women who had their throats slashed.
# Golden Label: entailment

restitution_premise = 58000
restitution_hypothesis = None # No specific amount mentioned in the hypothesis

# the hypothesis mentions restitution to two women who were victims of Proctor, which is also referenced in the premise
# however, the hypothesis does not mention the exact amount of restitution, which cannot be entailed from the premise
label = "neutral"

print(label)

