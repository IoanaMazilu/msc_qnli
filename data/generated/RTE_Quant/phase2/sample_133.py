# Premise: Of all the national park lands in the United States, none is closer to a major urban area or more beset with problems than the Everglades, a shallow, 50-mile-wide river of grass that flows south from Lake Okeechobee to Florida Bay. For more than a generation, this fragile natural wonder has been held hostage by a web of special interests -- farmers, sportsmen and about 6 million South Florida residents in need of drinking water and flood control -- that is as complex as the ecosystem itself.
# Hypothesis: The Everglades is 50-mile wide.
# Golden Label: entailment

everglades_width_premise = 50
everglades_width_hypothesis = 50

# the hypothesis talks about the width of the Everglades, which is also mentioned in the premise
if everglades_width_hypothesis != everglades_width_premise:
    # check if the width of the Everglades in the hypothesis contradicts the width from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

