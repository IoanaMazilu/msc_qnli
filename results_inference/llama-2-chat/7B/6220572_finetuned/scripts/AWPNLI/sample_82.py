total_pokemon_premise = 40.0
total_pokemon_hypothesis = 56.0

if total_pokemon_hypothesis <= total_pokemon_premise:
    # check if the number of Pokemon cards in the hypothesis contradicts the number of cards Mary had in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
