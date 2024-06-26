travelers_england_premise = 30
travelers_england_hypothesis = 70

travelers_france_premise = 26
travelers_france_hypothesis = 26

travelers_italy_premise = 32
travelers_italy_hypothesis = 32

# the hypothesis refers to the number of travelers to each country, mentioned in the premise
if travelers_england_hypothesis <= travelers_england_premise and travelers_france_hypothesis == travelers_france_premise and travelers_italy_hypothesis == travelers_italy_premise:
    # the hypothesis values for each country do not contradict the premise values
    label = "entailment"
elif travelers_england_hypothesis > travelers_england_premise or travelers_france_hypothesis!= travelers_france_premise or travelers_italy_hypothesis!= travelers_italy_premise:
    # the hypothesis values for at least one country contradict the premise values
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, but we cannot infer entailment, the relation is neutral
    label = "neutral"

print(label)
