n_americans_premise = 7/12
europeans_premise = 1/4
africans_premise = 2/9
asians_premise = 1/6
other_continents_premise = 50

n_americans_hypothesis = 1/12
europeans_hypothesis = 1/4
africans_hypothesis = 2/9
asians_hypothesis = 1/6
other_continents_hypothesis = 50

# calculate the total number of passengers in the premise
total_passengers_premise = n_americans_premise + europeans_premise + africans_premise + asians_premise + other_continents_premise

# calculate the total number of passengers in the hypothesis
total_passengers_hypothesis = n_americans_hypothesis + europeans_hypothesis + africans_hypothesis + asians_hypothesis + other_continents_hypothesis

# compare the total number of passengers in the premise and hypothesis
if total_passengers_premise <= total_passengers_hypothesis:
    # the hypothesis contradicts the premise, as the total number of passengers is higher in the hypothesis
    label = "contradiction"
elif total_passengers_hypothesis <= total_passengers_premise:
    # the premise contradicts the hypothesis, as the total number of passengers is lower in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are neutral, as the total number of passengers is the same in both
    label = "neutral"

print(label)
