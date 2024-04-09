cleaning_time_premise = 4
cleaning_time_hypothesis = 3

# the hypothesis talks about the time Bruce and Anne need to clean the house, which is also mentioned in the premise
if cleaning_time_hypothesis!= cleaning_time_premise:
    # check if the cleaning time in the hypothesis contradicts the cleaning time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
