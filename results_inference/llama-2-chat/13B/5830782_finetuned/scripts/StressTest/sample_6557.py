members_england_france_premise = 0
members_england_france_hypothesis = 0
members_england_italy_premise = 6
members_england_italy_hypothesis = 2
members_france_italy_premise = 11
members_france_italy_hypothesis = 11

# the hypothesis refers to the number of club members who traveled to England, France, Italy, as mentioned in the premise
if members_england_france_premise!= members_england_france_hypothesis:
    # check if the number of members who traveled to England and France in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif members_england_italy_premise!= members_england_italy_hypothesis:
    # check if the number of members who traveled to England and Italy in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif members_france_italy_premise!= members_france_italy_hypothesis:
    # check if the number of members who traveled to France and Italy in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
