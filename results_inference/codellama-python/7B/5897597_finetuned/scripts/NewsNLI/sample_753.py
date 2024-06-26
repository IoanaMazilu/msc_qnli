goals_mata_premise = 1
goals_lampard_premise = 1
goals_mata_hypothesis = 1
goals_lampard_hypothesis = 1

# the hypothesis mentions the goals of Juan Mata and Frank Lampard, which are also mentioned in the premise
if goals_mata_hypothesis!= goals_mata_premise:
    # check if the number of goals from Juan Mata in the hypothesis contradicts the number of goals from Juan Mata in the premise
    label = "contradiction"
elif goals_lampard_hypothesis!= goals_lampard_premise:
    # check if the number of goals from Frank Lampard from the hypothesis contradicts the number of goals from Frank Lampard in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
