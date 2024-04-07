# Premise: Every Sunday, Giri jogs 3 miles.
# Hypothesis: Every Sunday, Giri jogs less than 3 miles.
# Golden Label: contradiction

jogging_distance_premise = 3
jogging_distance_hypothesis = 3

# the hypothesis talks about Giri's jogging distance mentioned in the premise
if jogging_distance_hypothesis >= jogging_distance_premise:
    # check if the hypothesis value contradicts the 'less than jogging_distance_premise' statement
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise one, we can infer entailment
    label = "entailment"

print(label)

