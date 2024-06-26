seniors_premise = 300
cars_premise = 40
seniors_hypothesis = 800
cars_hypothesis = 40

# the hypothesis talks about the number of seniors and the percentage of cars owned
if seniors_hypothesis <= seniors_premise:
    # check if the hypothesis value contradicts the estimate of more than'seniors_premise'
    label = "contradiction"
elif cars_hypothesis!= cars_premise:
    # check if the percentage of cars owned in the hypothesis contradicts the percentage of cars owned reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
