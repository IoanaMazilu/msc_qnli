# Premise: If less than 4/12 of the passengers on a ship are from North America, 1/8 are Europeans, 1/3 are from Africa, 1/6 are from Asia and the remaining 35 people are citizens of other continents, then how many passengers are on board the ship?
# Hypothesis: If 1/12 of the passengers on a ship are from North America, 1/8 are Europeans, 1/3 are from Africa, 1/6 are from Asia and the remaining 35 people are citizens of other continents, then how many passengers are on board the ship?
# Golden Label: neutral

north_americans_premise = 4/12
north_americans_hypothesis = 1/12
europeans_premise = 1/8
europeans_hypothesis = 1/8
africans_premise = 1/3
africans_hypothesis = 1/3
asians_premise = 1/6
asians_hypothesis = 1/6
others_premise = 35
others_hypothesis = 35

# the hypothesis refers to the number of passengers from various continents mentioned in the premise
if north_americans_premise <= north_americans_hypothesis:
    # check if the percentage of North American passengers in the hypothesis contradicts the estimate in the premise
    label = "contradiction"
elif europeans_hypothesis != europeans_premise or africans_hypothesis != africans_premise or asians_hypothesis != asians_premise or others_hypothesis != others_premise:
    # check if the percentages of European, African, Asian passengers or the number of passengers from other continents in the hypothesis contradicts the numbers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

