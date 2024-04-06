# Premise: The dead included 11 inmates and six guards, Durango state public safety officials said in a statement.
# Hypothesis: 11 inmates and 6 guards are killed, Durango public safety officials report.
# Golden Label: entailment

dead_inmates_premise = 11
dead_inmates_hypothesis = 11
dead_guards_premise = 6
dead_guards_hypothesis = 6

# the hypothesis mentions the number of dead inmates and guards, which are also mentioned in the premise
if dead_inmates_hypothesis != dead_inmates_premise:
    # check if the number of dead inmates in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif dead_guards_hypothesis != dead_guards_premise:
    # check if the number of dead guards from the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

