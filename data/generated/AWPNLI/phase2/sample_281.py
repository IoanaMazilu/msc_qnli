# Premise: Maria picked 48.0 carrots from her garden, and she threw out 11.0 of them and then picked 15.0 more the next day.
# Hypothesis: She would have 50.0 carrots total.
# Golden Label: contradiction

picked_carrots_premise = 48.0
thrown_carrots_premise = 11.0
picked_next_day_premise = 15.0
total_carrots_hypothesis = 50.0

# the hypothesis refers to the total number of carrots, which are also mentioned in the premise
# compute the total number of carrots in the premise
total_carrots_premise = picked_carrots_premise - thrown_carrots_premise + picked_next_day_premise
if total_carrots_hypothesis != total_carrots_premise:
    # check if the number of carrots in the hypothesis contradicts the number of carrots from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

