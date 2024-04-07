# Premise: Efrida and Frazer who live less than 50 miles apart, meet at a restaurant that is directly north of Efrida's home and directly east of Frazer's home.
# Hypothesis: Efrida and Frazer who live 10 miles apart, meet at a restaurant that is directly north of Efrida's home and directly east of Frazer's home.
# Golden Label: neutral

distance_apart_premise = 50
distance_apart_hypothesis = 10

# the hypothesis refers to the distance between Efrida and Frazer's homes, mentioned also in the premise
if distance_apart_hypothesis > distance_apart_premise:
    # check if the hypothesis value contradicts the premise of less than 'distance_apart_premise'
    label = "contradiction"
elif distance_apart_hypothesis < distance_apart_premise:
    # the premise gives an upper limit for the distance between their homes
    # a distance less than 'distance_apart_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the distance in the hypothesis equals the distance in the premise, we can infer entailment
    label = "entailment"

print(label)

