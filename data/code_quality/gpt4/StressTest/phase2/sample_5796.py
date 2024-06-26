race_distance_premise = 1400
race_distance_hypothesis = 7400

# the hypothesis talks about the distance of a race run by Sam, Suresh, and Sanket, which is also stated in the premise
if race_distance_hypothesis < race_distance_premise:
    # check if the hypothesis value contradicts the specific distance of 'race_distance_premise'
    label = "contradiction"
elif race_distance_premise > race_distance_hypothesis:
    # check if the distance in the premise contradicts the maximum distance in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis distance does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
