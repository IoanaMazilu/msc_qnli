land_side_length_premise = 120
land_side_length_hypothesis = 220

# the hypothesis talks about the side length of the land, referenced also in the premise
if land_side_length_hypothesis!= land_side_length_premise:
    # check if the side length of the land in the hypothesis contradicts the side length of the land reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
