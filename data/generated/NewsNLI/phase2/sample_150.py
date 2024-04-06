# Premise: In fact, Wernick had only seen one zombie film before writing this script.
# Hypothesis: One of film's writers had seen just one zombie film in his life.
# Golden Label: entailment

zombie_film_seen_premise = 1
zombie_film_seen_hypothesis = 1

# the hypothesis mentions the number of zombie films seen by the writer, which is also mentioned in the premise
if zombie_film_seen_hypothesis != zombie_film_seen_premise:
    # check if the number of zombie films seen in the hypothesis contradicts the number of zombie films seen reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

