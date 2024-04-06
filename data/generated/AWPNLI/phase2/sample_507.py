# Premise: Marilyn has 51.0 bottle caps and Nancy gives her 36.0.
# Hypothesis: Marilyn has 84.0 bottle caps now.
# Golden Label: contradiction

initial_bottle_caps_premise = 51.0
given_bottle_caps_premise = 36.0
total_bottle_caps_hypothesis = 84.0

# the hypothesis refers to the total number of bottle caps, which is also mentioned in the premise
# compute the total number of bottle caps in the premise
total_bottle_caps_premise = initial_bottle_caps_premise + given_bottle_caps_premise
if total_bottle_caps_hypothesis != total_bottle_caps_premise:
    # check if the total number of bottle caps in the hypothesis contradicts the total number of bottle caps from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

