horseshoe_ponies_premise = 4/6
horseshoe_ponies_hypothesis = 5/6
icelandic_ponies_premise = 2/3
icelandic_ponies_hypothesis = 2/3

# the hypothesis refers to the proportion of ponies with horseshoes and the proportion of Icelandic ponies 
# mentioned in the premise

if horseshoe_ponies_premise >= horseshoe_ponies_hypothesis:
    # check if the proportion of 'horseshoe_ponies_hypothesis' contradicts the proportion of horseshoe ponies in the premise
    label = "contradiction"
elif icelandic_ponies_hypothesis != icelandic_ponies_premise:
    # check if the proportion of Icelandic ponies in the hypothesis contradicts the proportion of Icelandic ponies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and proportions do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
