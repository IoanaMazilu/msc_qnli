# Premise: During Reinsdorf's 24 seasons as chairman of the White Sox, the team has captured American League division championships three times, including an AL Central title in 2000.
# Hypothesis: The White Sox have won 24 championships.
# Golden Label: neutral

reinsdorf_seasons_premise = 24
championships_premise = 3
championships_hypothesis = 24

# the hypothesis talks about the total number of championships won by the White Sox, which is also mentioned in the premise
if championships_hypothesis != championships_premise:
    # check if the number of championships in the hypothesis contradicts the number of championships from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
