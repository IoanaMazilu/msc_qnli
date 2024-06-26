counter_demonstration_premise = 25
counter_demonstration_hypothesis = 25

# the hypothesis talks about the counter-demonstration of Palestinians, which is also mentioned in the premise
if counter_demonstration_hypothesis!= counter_demonstration_premise:
    # check if the number of people in the counter-demonstration in the hypothesis contradicts the number of people from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
