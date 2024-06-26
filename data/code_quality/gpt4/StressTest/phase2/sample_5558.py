horseshoes_ponies_premise = 5/7
horseshoes_ponies_hypothesis = 2/7
icelandic_ponies_with_horseshoes_premise = 2/3
icelandic_ponies_with_horseshoes_hypothesis = 2/3

# the hypothesis talks about the proportions of ponies with horseshoes and the proportions of Icelandic ponies with horseshoes
if horseshoes_ponies_hypothesis != horseshoes_ponies_premise:
    # check if the hypothesis value contradicts the exact proportion of ponies with horseshoes in the premise
    label = "contradiction"
elif icelandic_ponies_with_horseshoes_hypothesis != icelandic_ponies_with_horseshoes_premise:
    # check if the hypothesis value contradicts the exact proportion of Icelandic ponies with horseshoes in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
