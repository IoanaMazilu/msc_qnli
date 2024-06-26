starting_caps_jose = 7.0
given_caps_jose = 2.0
remaining_caps_hypothesis = 4.0

# the hypothesis refers to the number of remaining bottle caps, which can be computed from the premise
# compute the remaining bottle caps in the premise
remaining_caps_premise = starting_caps_jose - given_caps_jose
if remaining_caps_hypothesis != remaining_caps_premise:
    # check if the remaining caps in the hypothesis contradicts the remaining caps from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
