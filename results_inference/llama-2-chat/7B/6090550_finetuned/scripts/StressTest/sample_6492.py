if_premise = 3
if_hypothesis = 7

if if_premise >= if_hypothesis:
    # the hypothesis refers to the percentage of money that Dana gives back to her parents
    # this is also mentioned in the premise
    # but the hypothesis specifies a lower percentage, which contradicts the premise
    label = "contradiction"
elif if_premise < if_hypothesis:
    # the premise specifies a percentage of money that Dana gives back to her parents
    # the hypothesis specifies a lower percentage, which is consistent with the premise
    # but the premise does not explicitly state the percentage in the hypothesis
    # thus, the relation is neutral
    label = "neutral"
else:
    # if the hypothesis percentage is equal to the premise percentage, then the hypothesis is entailed
    # since the premise does not explicitly state the percentage in the hypothesis, we cannot say that the premise entails the hypothesis
    # thus, the relation is neutral
    label = "neutral"

print(label)
