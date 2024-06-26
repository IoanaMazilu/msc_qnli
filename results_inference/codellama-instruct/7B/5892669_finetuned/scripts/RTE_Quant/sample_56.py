injured_persons_premise = 2
attacks_premise = 2
branches_premise = 2

attackers_hypothesis = 2
branches_hypothesis = 2

# the hypothesis talks about the number of attackers and the number of bank branches which are not referenced in the premise
# the hypothesis cannot be entailed from the premise, since the number of attackers and the number of bank branches is unknown.
label = "neutral"

print(label)
