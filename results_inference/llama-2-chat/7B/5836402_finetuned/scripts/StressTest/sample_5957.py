members_england_premise = 26
members_england_hypothesis = 86
members_france_premise = 26
members_france_hypothesis = 26
members_italy_premise = 32
members_italy_hypothesis = 32

# the hypothesis refers to the number of members that traveled to certain countries, which are also mentioned in the premise
if members_england_hypothesis!= members_england_premise:
    # check if the number of members in England in the hypothesis contradicts the number of members in England reported in the premise
    label = "contradiction"
elif members_france_hypothesis!= members_france_premise:
    # check if the number of members in France in the hypothesis contradicts the number of members in France reported in the premise
    label = "contradiction"
elif members_italy_hypothesis!= members_italy_premise:
    # check if the number of members in Italy in the hypothesis contradicts the number of members in Italy reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
