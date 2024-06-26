ponies_horseshoes_premise = 5/7
ponies_horseshoes_hypothesis = 3/7
ponies_iceland_premise = 2/3
ponies_iceland_hypothesis = 2/3

# the hypothesis refers to the fraction of ponies with horseshoes and the fraction of ponies from Iceland mentioned in the premise
if ponies_horseshoes_premise <= ponies_horseshoes_hypothesis:
    # check if the hypothesis value contradicts the exact fraction of ponies with horseshoes in the premise
    label = "contradiction"
elif ponies_iceland_hypothesis != ponies_iceland_premise:
    # check if the fraction of Icelandic ponies in the hypothesis contradicts the fraction of Icelandic ponies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
