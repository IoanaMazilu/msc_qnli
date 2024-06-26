members_england_france_premise = 8
members_england_italy_premise = 0
members_france_italy_premise = 11

members_england_france_hypothesis = 6
members_england_italy_hypothesis = 0
members_france_italy_hypothesis = 11

# the hypothesis refers to the number of members that traveled to both England and France, Italy
if members_england_france_hypothesis!= members_england_france_premise:
    # check if the number of members in the hypothesis contradicts the number of members in the premise
    label = "contradiction"
elif members_england_italy_hypothesis!= members_england_italy_premise:
    # check if the number of members in the hypothesis contradicts the number of members in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
