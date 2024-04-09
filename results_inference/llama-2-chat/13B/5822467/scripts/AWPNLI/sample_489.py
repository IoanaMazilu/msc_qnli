bottle_caps_premise = 7.0
bottle_caps_given_premise = 2.0
left_caps_hypothesis = 4.0

# compute the total number of bottle caps in the premise
total_caps_premise = bottle_caps_premise + bottle_caps_given_premise

if left_caps_hypothesis < total_caps_premise:
    # check if the number of left bottle caps in the hypothesis contradicts the estimate of more than 'bottle_caps_given_premise'
    label = "contradiction"
elif left_caps_hypothesis!= total_caps_premise:
    # check if the number of left bottle caps in the hypothesis contradicts the number of bottle caps in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
