num_birds_premise = 12.0
num_birds_fly_away_premise = 8.0
num_birds_hypothesis = 4.0

# the hypothesis refers to the number of birds on the fence, which are also mentioned in the premise
# compute the total number of birds on the fence
total_num_birds_premise = num_birds_premise - num_birds_fly_away_premise
if total_num_birds_premise!= num_birds_hypothesis:
    # check if the number of birds in the hypothesis contradicts the number of birds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
