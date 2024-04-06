# Premise: The Motion Picture Association of America (MPAA) said the civil suits would seek damages of up to $30,000 per film.
# Hypothesis: The law states $30,000 damages can be sought per film.
# Golden Label: neutral

damage_premise = 30000
damage_hypothesis = 30000

# the hypothesis talks about the amount of damages that can be sought per film, which is also mentioned in the premise

if damage_hypothesis != damage_premise:
    # check if the amount of damages in the hypothesis contradicts the amount of damages from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

