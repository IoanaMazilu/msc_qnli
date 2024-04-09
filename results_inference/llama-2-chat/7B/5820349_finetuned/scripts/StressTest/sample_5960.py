england_france_travel_premise = 6
england_france_travel_hypothesis = 3
england_italy_travel_premise = 0
england_italy_travel_hypothesis = 0
france_italy_travel_premise = 11
france_italy_travel_hypothesis = 11

# the hypothesis talks about the number of club members who traveled to England, France, Italy, and both countries, referenced also in the premise
if england_france_travel_hypothesis!= england_france_travel_premise:
    # check if the number of members who traveled to England and France in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif england_italy_travel_hypothesis!= england_italy_travel_premise:
    # check if the number of members who traveled to England and Italy in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif france_italy_travel_hypothesis!= france_italy_travel_premise:
    # check if the number of members who traveled to France and Italy in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
