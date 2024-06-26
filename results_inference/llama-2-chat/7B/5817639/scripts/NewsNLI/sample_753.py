pressure_premise = "lost to bottom side QPR and drew with newly-promoted Southampton in their last two home games"
pressure_hypothesis = "help Chelsea defeat Arsenal 2-1"

# the hypothesis mentions the goals from Juan Mata and Frank Lampard, which are also mentioned in the premise
if pressure_hypothesis == pressure_premise:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"
elif Juan_Mata_hypothesis!= Juan_Mata_premise or Frank_Lampard_hypothesis!= Frank_Lampard_premise:
    # check if the goal scorers in the hypothesis contradict the goal scorers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
