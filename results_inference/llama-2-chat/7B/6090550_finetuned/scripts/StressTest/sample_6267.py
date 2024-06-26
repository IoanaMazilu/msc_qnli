percentage_dead_premise = 10
percentage_dead_hypothesis = 30
percentage_left_premise = 20
percentage_left_hypothesis = 20

# the hypothesis talks about the percentage of people who died and left the village, both referenced in the premise
if percentage_dead_hypothesis < percentage_dead_premise:
    # check if the hypothesis value contradicts the percentage of people who died in the premise
    label = "contradiction"
elif percentage_left_hypothesis!= percentage_left_premise:
    # check if the percentage of people who left the village in the hypothesis contradicts the percentage of people who left the village in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
