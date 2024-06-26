german_premise = "Borussia Dortmund routed Moenchengladbach 5-0"
german_hypothesis = "Borussia Dortmund up to third after 5-0 rout of Moenchengladbach"

# the hypothesis mentions the number of goals scored by Borussia Dortmund, which is also mentioned in the premise
if german_hypothesis!= german_premise:
    # check if the number of goals scored by Borussia Dortmund in the hypothesis contradicts the number of goals scored in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
