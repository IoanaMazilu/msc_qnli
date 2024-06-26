distance_premise = 35
distance_hypothesis = 15

# the hypothesis talks about the distance between the homes of Efrida and Frazer, referenced also in the premise
if distance_hypothesis > distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the distance in the hypothesis is equal to the one in the premise, we can infer entailment
    label = "entailment"

print(label)
