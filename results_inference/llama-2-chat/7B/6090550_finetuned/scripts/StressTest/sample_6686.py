somenumber_premise = 60
some_seconds_premise = 40
steps_climbed_hypothesis = 80
seconds_hypothesis = 40

# the hypothesis talks about the number of steps climbed by Vinod, which is also mentioned in the premise
if steps_climbed_hypothesis!= somenumber_premise:
    # check if the number of steps in the hypothesis contradicts the number of steps reported in the premise
    label = "contradiction"
elif seconds_hypothesis!= seconds_premise:
    # check if the time taken to climb the steps in the hypothesis contradicts the time taken reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
