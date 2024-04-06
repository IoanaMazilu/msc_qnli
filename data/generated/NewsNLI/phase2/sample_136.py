# Premise: The La Paz urban gondola will consist of three separate service lines stretching across a combined 10.7 kilometer (6.1 mile) area of the city.
# Hypothesis: An urban gondola 10.7 kilometers in length is being designed and built in the Bolivian city of La Paz.
# Golden Label: neutral

gondola_length_premise = 10.7
gondola_length_hypothesis = 10.7

# the hypothesis mentions the length of the gondola in La Paz, which is also mentioned in the premise
if gondola_length_hypothesis != gondola_length_premise:
    # check if the gondola length in the hypothesis contradicts the gondola length reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

