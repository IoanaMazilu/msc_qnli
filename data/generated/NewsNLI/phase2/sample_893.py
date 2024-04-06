# Premise: But they were given a tough fight by underdogs Italy, who were inspired by an 80,000 crowd in a stadium normally reserved for Serie A giants Inter and AC Milan.
# Hypothesis: A massive crowd of 80,000 watched the game in San Siro stadium.
# Golden Label: neutral

crowd_premise = 80000
crowd_hypothesis = 80000

# The hypothesis mentions the crowd number which is also mentioned in the premise.
# However, the hypothesis mentions the stadium name which is not explicitly stated in the premise.

if crowd_hypothesis != crowd_premise:
    # check if the crowd number in the hypothesis contradicts the crowd number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, but cannot be fully entailed either, we infer neutrality
    label = "neutral"

print(label)

