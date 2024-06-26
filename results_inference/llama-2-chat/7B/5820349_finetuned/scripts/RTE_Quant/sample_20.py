wars_pakistan_india_premise = 2
wars_pakistan_india_hypothesis = 3

# the hypothesis talks about the number of wars fought by Pakistan and India, which is also mentioned in the premise
if wars_pakistan_india_hypothesis!= wars_pakistan_india_premise:
    # check if the number of wars in the hypothesis contradicts the number of wars from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
