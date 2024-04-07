# Premise: Exactly less than 8/7 of the ponies have horseshoes, and exactly 2/3 of the ponies with horseshoes are from Iceland.
# Hypothesis: Exactly 5/7 of the ponies have horseshoes, and exactly 2/3 of the ponies with horseshoes are from Iceland.
# Golden Label: neutral

ponies_horseshoes_premise = 8/7
ponies_horseshoes_hypothesis = 5/7
ponies_iceland_premise = 2/3
ponies_iceland_hypothesis = 2/3

# the hypothesis refers to the number of ponies with horseshoes and the number of ponies from Iceland mentioned in the premise
if ponies_horseshoes_hypothesis > ponies_horseshoes_premise:
    # check if the fraction of 'ponies_horseshoes_hypothesis' contradicts the fraction of ponies with horseshoes in the premise
    label = "contradiction"
elif ponies_iceland_hypothesis != ponies_iceland_premise:
    # check if the fraction of ponies from Iceland in the hypothesis contradicts the fraction of ponies from Iceland reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

