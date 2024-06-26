distance_apart_premise = 10
distance_apart_hypothesis = 50

# the hypothesis refers to the distance between Efrida and Frazer's homes mentioned in the premise
if distance_apart_hypothesis < distance_apart_premise:
    # check if 'distance_apart_hypothesis' contradicts the distance reported in the premise
    label = "contradiction"
elif distance_apart_hypothesis == distance_apart_premise:
    # check if 'distance_apart_hypothesis' can be fully and explicitly entailed from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
