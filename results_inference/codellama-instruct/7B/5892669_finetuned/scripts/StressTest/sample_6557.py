travel_england_france_premise = 0
travel_england_france_hypothesis = 0
travel_england_italy_premise = 6
travel_england_italy_hypothesis = 2
travel_france_italy_premise = 11
travel_france_italy_hypothesis = 11

# the hypothesis refers to the number of club members who traveled to England, France, Italy, and both England and Italy mentioned in the premise
if travel_england_france_premise!= travel_england_france_hypothesis:
    # check if the number of members who traveled to England and France in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif travel_england_italy_premise!= travel_england_italy_hypothesis:
    # check if the number of members who traveled to England and Italy in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif travel_france_italy_premise!= travel_france_italy_hypothesis:
    # check if the number of members who traveled to France and Italy in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
