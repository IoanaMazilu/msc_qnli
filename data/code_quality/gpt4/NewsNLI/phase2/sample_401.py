civilians_dead_premise = 21
civilians_beheaded_premise = 2
civilians_dead_hypothesis = 21
civilians_beheaded_hypothesis = 2

# the hypothesis mentions the number of dead civilians and beheaded ones, which are also mentioned in the premise
if civilians_dead_hypothesis != civilians_dead_premise:
    # check if the number of dead civilians in the hypothesis contradicts the number of dead civilians reported in the premise
    label = "contradiction"
elif civilians_beheaded_hypothesis != civilians_beheaded_premise:
    # check if the number of beheaded civilians from the hypothesis contradicts the number of beheaded civilians in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
