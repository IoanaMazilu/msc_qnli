people_dead_premise = 10000
people_displaced_premise = 500000
people_dead_hypothesis = 200000
people_displaced_hypothesis = 2500000

# the hypothesis mentions the number of people who died and were displaced, which are also mentioned in the premise
if people_dead_hypothesis > people_dead_premise:
    # check if the number of people who died according to the hypothesis contradicts the number provided in the premise
    label = "contradiction"
elif people_displaced_hypothesis > people_displaced_premise:
    # check if the number of people who were displaced according to the hypothesis contradicts the number provided in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
