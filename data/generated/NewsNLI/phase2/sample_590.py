# Premise: But Vodianova has a dream that could n't be further from the glitzy world of fashion -- to build 500 play parks in her native Russia.
# Hypothesis: Her dream is for the foundation to build 500 play parks across Russia.
# Golden Label: neutral

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

