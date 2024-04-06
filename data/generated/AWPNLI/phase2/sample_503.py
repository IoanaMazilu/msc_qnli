# Premise: There are 35.0 bottle caps in every box of Beverly's bottle cap collection, and the bottle caps are organized into 7.0 boxes.
# Hypothesis: 244.0 bottle caps are there in total.
# Golden Label: contradiction

caps_per_box_premise = 35.0
box_num_premise = 7.0
total_caps_hypothesis = 244.0

# the hypothesis refers to the total number of bottle caps, which is also mentioned in the premise
# compute the total number of bottle caps in the premise
total_caps_premise = caps_per_box_premise * box_num_premise
if total_caps_hypothesis != total_caps_premise:
    # check if the total number of bottle caps in the hypothesis contradicts the total number of bottle caps from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

