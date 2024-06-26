bottle_caps_premise = 7.0
bottle_caps_given = 2.0
bottle_caps_left_hypothesis = 4.0

# the hypothesis refers to the number of bottle caps left, which are also mentioned in the premise
# compute the total number of bottle caps left in the premise
bottle_caps_left_premise = bottle_caps_premise - bottle_caps_given
if bottle_caps_left_hypothesis!= bottle_caps_left_premise:
    # check if the number of bottle caps left in the hypothesis contradicts the number of bottle caps left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
