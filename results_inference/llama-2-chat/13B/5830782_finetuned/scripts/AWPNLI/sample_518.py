birds_premise = 6.0
nests_premise = 3.0
bird_related_objects_hypothesis = 9.0

# the hypothesis refers to the total number of bird-related objects, which is also mentioned in the premise
# compute the total number of bird-related objects in the premise
total_bird_related_objects_premise = birds_premise + nests_premise
if bird_related_objects_hypothesis!= total_bird_related_objects_premise:
    # check if the total number of bird-related objects in the hypothesis contradicts the total number of bird-related objects from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
