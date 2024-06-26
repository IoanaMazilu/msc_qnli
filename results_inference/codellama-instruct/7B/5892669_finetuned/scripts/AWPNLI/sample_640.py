fish_premise = 212.0
moved_fish_premise = 68.0
left_fish_hypothesis = 144.0

# the hypothesis refers to the number of fish left in the first tank, which is also mentioned in the premise
# compute the number of fish left in the first tank in the premise
left_fish_premise = fish_premise - moved_fish_premise
if left_fish_hypothesis!= left_fish_premise:
    # check if the number of fish left in the hypothesis contradicts the number of fish left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
