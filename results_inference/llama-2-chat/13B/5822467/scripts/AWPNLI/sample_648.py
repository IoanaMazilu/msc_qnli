oranges_premise = 45.0
bag_size_premise = 23.0
bags_hypothesis = 1.95652173913

# compute the total number of oranges in the premise
total_oranges_premise = oranges_premise * bag_size_premise

# compute the total number of oranges in the hypothesis
total_oranges_hypothesis = bags_hypothesis * bag_size_premise

if total_oranges_hypothesis!= total_oranges_premise:
    # check if the number of oranges in the hypothesis contradicts the number of oranges from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
