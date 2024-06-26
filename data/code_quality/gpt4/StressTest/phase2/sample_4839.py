ponies_horseshoes_premise = 3/10
ponies_horseshoes_hypothesis = 2/10
ponies_horseshoes_iceland_premise = 5/8
ponies_horseshoes_iceland_hypothesis = 5/8

# The hypothesis refers to both the proportion of ponies with horseshoes and the proportion of those that are from Iceland
if ponies_horseshoes_premise <= ponies_horseshoes_hypothesis:
    # Check if the hypothesis contradicts the premise regarding the proportion of ponies with horseshoes
    label = "contradiction"
elif ponies_horseshoes_iceland_hypothesis != ponies_horseshoes_iceland_premise:
    # Check if the hypothesis contradicts the premise regarding the proportion of ponies with horseshoes that are from Iceland
    label = "contradiction"
else:
    # If the hypothesis does not contradict the premise in any way, we can infer entailment
    label = "entailment"

print(label)
