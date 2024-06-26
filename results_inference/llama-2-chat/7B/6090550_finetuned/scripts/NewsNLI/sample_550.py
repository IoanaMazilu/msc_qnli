# The hypothesis mentions the brightness of the fireball, which is also mentioned in the premise
brightness_premise = 5
brightness_hypothesis = 5

# the hypothesis does not provide any information about the size or weight of the meteor
size_weight_premise = 0
size_weight_hypothesis = 0

# the hypothesis and premise mention the size and weight of the meteor, but do not provide any information about the estimated size and weight
size_weight_premise = 0
size_weight_hypothesis = 0

# the hypothesis and premise mention the estimated size and weight of the meteor, but do not provide any information about the actual size and weight
actual_size_weight_premise = 0
actual_size_weight_hypothesis = 0

# the hypothesis and premise mention the brightness of the fireball, which is not mentioned in the hypothesis
brightness_premise_contradiction = 0

# the hypothesis and premise do not provide any information about the actual size and weight of the meteor, which can be estimated from the premise
actual_size_weight_contradiction = 0

# the hypothesis and premise do not provide any information about the estimated size and weight of the meteor, which can be estimated from the premise
estimated_size_weight_contradiction = 0

# the hypothesis and premise do not provide any information about the brightness of the fireball, which is mentioned in the premise
brightness_contradiction = 0

# if the hypothesis and premise contradict each other, the relation is contradiction
if brightness_premise!= brightness_hypothesis:
    relation = "contradiction"
elif size_weight_premise!= size_weight_hypothesis:
    relation = "contradiction"
elif actual_size_weight_premise!= actual_size_weight_hypothesis:
    relation = "contradiction"
elif brightness_premise_contradiction!= brightness_contradiction:
    relation = "contradiction"
elif estimated_size_weight_contradiction!= brightness_contradiction:
    relation = "contradiction"
else:
    relation = "neutral"

print(relation)
