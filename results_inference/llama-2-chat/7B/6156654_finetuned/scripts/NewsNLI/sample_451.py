animals_killed_premise = 48
animals_killed_hypothesis = 48
primates_killed_premise = 2
primates_killed_hypothesis = 2

# the hypothesis talks about the number of animals killed by law enforcement, which is also mentioned in the premise
if animals_killed_hypothesis!= animals_killed_premise:
    # check if the number of animals killed by law enforcement in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif primates_killed_hypothesis!= primates_killed_premise:
    # check if the number of primates killed by the other animals in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
