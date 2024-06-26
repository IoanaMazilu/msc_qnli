girls_premise = 542.0
boys_premise = 387.0
girls_hypothesis = 155.0

# the hypothesis refers to the number of girls, which is also mentioned in the premise
# compute the total number of girls in the premise
total_girls_premise = girls_premise + girls_hypothesis
if total_girls_premise!= girls_premise:
    # check if the number of girls in the hypothesis contradicts the number of girls from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
