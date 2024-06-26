total_candy_premise = 47.0 + 25.0 + 40.0
total_candy_hypothesis = 65.0

# the hypothesis refers to the total number of candy, which is also mentioned in the premise
# check if the total number of candy in the hypothesis contradicts the total number of candy from the premise
if total_candy_hypothesis!= total_candy_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
