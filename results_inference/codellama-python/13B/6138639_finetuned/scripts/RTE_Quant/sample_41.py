min_percentage_premise = 5
max_percentage_premise = 10
min_percentage_hypothesis = 5
max_percentage_hypothesis = 10

# the hypothesis talks about the percentage of stolen art that gets returned to the owners, which is also mentioned in the premise
if min_percentage_hypothesis!= min_percentage_premise or max_percentage_hypothesis!= max_percentage_premise:
    # check if the percentage range in the hypothesis contradicts the percentage range in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
