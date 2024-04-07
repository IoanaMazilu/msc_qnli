# Premise: Exactly 3/10 of the ponies have horseshoes, and exactly 5/8 of the ponies with horseshoes are from Iceland.
# Hypothesis: Exactly less than 3/10 of the ponies have horseshoes, and exactly 5/8 of the ponies with horseshoes are from Iceland.
# Golden Label: contradiction

ponies_horseshoes_premise = 3/10
ponies_horseshoes_hypothesis = 3/10
ponies_iceland_premise = 5/8
ponies_iceland_hypothesis = 5/8

# the hypothesis refers to the number of ponies with horseshoes and ponies from Iceland mentioned in the premise
if ponies_horseshoes_hypothesis >= ponies_horseshoes_premise:
    # check if the estimate of 'ponies_horseshoes_hypothesis' contradicts the number of ponies with horseshoes in the premise
    label = "contradiction"
elif ponies_iceland_hypothesis != ponies_iceland_premise:
    # check if the number of ponies from Iceland in the hypothesis contradicts the number of ponies from Iceland reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

