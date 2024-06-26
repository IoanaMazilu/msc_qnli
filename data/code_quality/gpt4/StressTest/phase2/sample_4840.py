ponies_horseshoes_premise = 2/10
ponies_horseshoes_hypothesis = 3/10
ponies_iceland_premise = 5/8
ponies_iceland_hypothesis = 5/8

# the hypothesis refers to the proportion of ponies with horseshoes and the proportion of ponies from Iceland with horseshoes 
if ponies_horseshoes_hypothesis <= ponies_horseshoes_premise:
    # check if the hypothesis value contradicts the premise of more than 'ponies_horseshoes_premise' ponies having horseshoes
    label = "contradiction"
elif ponies_iceland_hypothesis != ponies_iceland_premise:
    # check if the proportion of ponies from Iceland with horseshoes in the hypothesis contradicts the proportion in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the proportion of ponies with horseshoes
    # any proportion larger than 'ponies_horseshoes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
