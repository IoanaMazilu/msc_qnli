bottles_maria_premise = 45.0
bottles_drank_maria_premise = 14.0
bottles_drank_sister_premise = 8.0
total_bottles_premise = bottles_maria_premise + bottles_drank_maria_premise + bottles_drank_sister_premise
bottles_left_hypothesis = 23.0

# the hypothesis refers to the number of bottles left, which are also mentioned in the premise
# compute the total number of bottles in the premise
total_bottles_premise = bottles_maria_premise + bottles_drank_maria_premise + bottles_drank_sister_premise
if bottles_left_hypothesis >= total_bottles_premise:
    # check if the number of bottles left in the hypothesis is greater than or equal to the total number of bottles in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer contradiction
    label = "contradiction"

print(label)
