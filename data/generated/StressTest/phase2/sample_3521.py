# Premise: Exactly 5/7 of the ponies have horseshoes, and exactly 2/3 of the ponies with horseshoes are from Iceland.
# Hypothesis: Exactly 3/7 of the ponies have horseshoes, and exactly 2/3 of the ponies with horseshoes are from Iceland.
# Golden Label: contradiction

horseshoes_ponies_premise = 5/7
horseshoes_ponies_hypothesis = 3/7
icelandic_horseshoed_ponies_premise = 2/3
icelandic_horseshoed_ponies_hypothesis = 2/3

# the hypothesis refers to the fraction of ponies with horseshoes and the fraction of ponies from Iceland with horseshoes, both mentioned in the premise
if horseshoes_ponies_premise != horseshoes_ponies_hypothesis:
    # check if the fraction of ponies with horseshoes in the hypothesis contradicts the fraction of ponies with horseshoes reported in the premise
    label = "contradiction"
elif icelandic_horseshoed_ponies_hypothesis != icelandic_horseshoed_ponies_premise:
    # check if the fraction of ponies from Iceland with horseshoes in the hypothesis contradicts the fraction of ponies from Iceland with horseshoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

