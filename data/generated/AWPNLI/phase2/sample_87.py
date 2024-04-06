# Premise: There are 7.0 bottle caps in a box and Linda puts 7.0 more bottle caps inside.
# Hypothesis: 18.0 bottle caps are in the box.
# Golden Label: contradiction

bottle_caps_premise = 7.0
added_bottle_caps_premise = 7.0
total_bottle_caps_hypothesis = 18.0

# the hypothesis refers to the total number of bottle caps in the box, which is also mentioned in the premise
# compute the total number of bottle caps in the premise
total_bottle_caps_premise = bottle_caps_premise + added_bottle_caps_premise
if total_bottle_caps_hypothesis != total_bottle_caps_premise:
    # check if the total number of bottle caps in the hypothesis contradicts the total number of bottle caps from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

