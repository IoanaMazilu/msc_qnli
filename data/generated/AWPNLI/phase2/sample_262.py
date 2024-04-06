# Premise: Mrs. Hilt impressed 2436.0 fans at the basketball game on Friday, and the fans were seated in equal groups on 3.0 sets of bleachers.
# Hypothesis: 812.0 fans were on each set.
# Golden Label: entailment

fans_premise = 2436.0
sets_premise = 3.0
fans_per_set_hypothesis = 812.0

# the hypothesis refers to the number of fans per set, which can be calculated from the premise
# compute the number of fans per set in the premise
fans_per_set_premise = fans_premise / sets_premise
if fans_per_set_hypothesis != fans_per_set_premise:
    # check if the number of fans per set in the hypothesis contradicts the number of fans per set from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

