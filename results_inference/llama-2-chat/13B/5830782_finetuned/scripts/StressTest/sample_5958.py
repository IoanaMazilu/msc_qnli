members_england_france_premise = 6
members_england_france_hypothesis = 8
members_england_italy_premise = 0
members_england_italy_hypothesis = 0
members_france_italy_premise = 11
members_france_italy_hypothesis = 11

# the hypothesis talks about the number of club members who traveled to England, France, Italy, referenced also in the premise
if members_england_france_hypothesis <= members_england_france_premise:
    # check if the hypothesis value contradicts the number of members who traveled to England and France in the premise
    label = "contradiction"
elif members_england_italy_hypothesis!= members_england_italy_premise or members_france_italy_hypothesis!= members_france_italy_premise:
    # check if the number of members who traveled to England and Italy or France and Italy in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
