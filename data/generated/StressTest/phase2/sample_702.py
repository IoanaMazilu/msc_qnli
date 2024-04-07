# Premise: Exactly 5/6 of the ponies have horseshoes, and exactly 2/3 of the ponies with horseshoes are from Iceland.
# Hypothesis: Exactly more than 4/6 of the ponies have horseshoes, and exactly 2/3 of the ponies with horseshoes are from Iceland.
# Golden Label: entailment

ponies_horseshoes_premise = 5/6
ponies_horseshoes_hypothesis = 4/6
ponies_iceland_premise = 2/3
ponies_iceland_hypothesis = 2/3

# the hypothesis refers to the ratio of ponies with horseshoes and from Iceland mentioned in the premise
if ponies_horseshoes_hypothesis >= ponies_horseshoes_premise:
    # check if the estimate of 'ponies_horseshoes_hypothesis' contradicts the exact ratio of ponies with horseshoes in the premise
    label = "contradiction"
elif ponies_iceland_hypothesis != ponies_iceland_premise:
    # check if the ratio of ponies from Iceland in the hypothesis contradicts the exact ratio of ponies from Iceland reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

