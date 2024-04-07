# Premise: Exactly more than 3/7 of the ponies have horseshoes, and exactly 2/3 of the ponies with horseshoes are from Iceland.
# Hypothesis: Exactly 5/7 of the ponies have horseshoes, and exactly 2/3 of the ponies with horseshoes are from Iceland.
# Golden Label: neutral

horseshoes_ponies_premise = 3/7
horseshoes_ponies_hypothesis = 5/7
iceland_horseshoes_ponies_premise = 2/3
iceland_horseshoes_ponies_hypothesis = 2/3

# the hypothesis refers to the part of ponies with horseshoes and the part of ponies from Iceland with horseshoes, both mentioned in the premise
if horseshoes_ponies_hypothesis != horseshoes_ponies_premise:
    # check if the portion of ponies with horseshoes in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
elif iceland_horseshoes_ponies_hypothesis != iceland_horseshoes_ponies_premise:
    # check if the portion of Icelandic ponies with horseshoes in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

