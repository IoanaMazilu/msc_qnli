parks_premise = 500
parks_hypothesis = 500

# the hypothesis mentions the number of play parks to be built in Russia, which is also mentioned in the premise
if parks_hypothesis != parks_premise:
    # check if the number of parks in the hypothesis contradicts the number of parks reported in the premise
    label = "contradiction"
else:
    # if the number of parks in the hypothesis does not contradict the number of parks in the premise, we can infer entailment
    label = "entailment"

print(label)
