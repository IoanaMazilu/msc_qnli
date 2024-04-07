# Premise: Joke is faster than Paul, Joke and Paul each walk 24 KM.
# Hypothesis: Joke is faster than Paul, Joke and Paul each walk more than 14 KM.
# Golden Label: entailment

distance_walked_by_joke_paul_premise = 24
distance_walked_by_joke_paul_hypothesis = 14

# the hypothesis talks about the distance that Joke and Paul have walked, which is also mentioned in the premise
if distance_walked_by_joke_paul_hypothesis >= distance_walked_by_joke_paul_premise:
    # check if the hypothesis value contradicts the exact distance walked by Joke and Paul reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

