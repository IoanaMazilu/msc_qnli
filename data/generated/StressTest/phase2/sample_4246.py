# Premise: Exactly more than 1/10 of the ponies have horseshoes, and exactly 5/8 of the ponies with horseshoes are from Iceland.
# Hypothesis: Exactly 3/10 of the ponies have horseshoes, and exactly 5/8 of the ponies with horseshoes are from Iceland.
# Golden Label: neutral

ponies_horseshoes_premise = 1/10
ponies_horseshoes_hypothesis = 3/10
ponies_iceland_premise = 5/8
ponies_iceland_hypothesis = 5/8

# the hypothesis refers to the proportion of ponies with horseshoes and the proportion of these that are from Iceland
if ponies_horseshoes_hypothesis <= ponies_horseshoes_premise:
    # check if the proportion in the hypothesis contradicts the estimate of more than 'ponies_horseshoes_premise'
    label = "contradiction"
elif ponies_iceland_hypothesis != ponies_iceland_premise:
    # check if the proportion of ponies from Iceland in the hypothesis contradicts the proportion reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the proportion of ponies with horseshoes
    # a proportion greater than 'ponies_horseshoes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

