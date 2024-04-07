# Premise: Exactly 3/10 of the ponies have horseshoes, and exactly 5/8 of the ponies with horseshoes are from Iceland.
# Hypothesis: Exactly more than 1/10 of the ponies have horseshoes, and exactly 5/8 of the ponies with horseshoes are from Iceland.
# Golden Label: entailment

ponies_horseshoes_premise = 3/10
ponies_horseshoes_hypothesis = 1/10
ponies_iceland_premise = 5/8
ponies_iceland_hypothesis = 5/8

# the hypothesis refers to the proportion of ponies with horseshoes and the proportion of Icelandic ponies among those,
# both mentioned in the premise
if ponies_horseshoes_premise <= ponies_horseshoes_hypothesis:
    # check if the proportion in 'ponies_horseshoes_hypothesis' contradicts the proportion in the premise
    label = "contradiction"
elif ponies_iceland_hypothesis != ponies_iceland_premise:
    # check if the proportion of Icelandic ponies in the hypothesis contradicts the proportion reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

