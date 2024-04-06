# Premise: Last week, saw the fall of the Dutch right wing coalition government, made up of the Christian-democrats (CDA) led by Prime Minister Jan Peter Balkenende, the right wing liberal party (VVD) and the so-called left-liberal D66.
# Hypothesis: Three parties form a Dutch coalition government.
# Golden Label: entailment

parties_in_coalition_premise = 3
parties_in_coalition_hypothesis = 3

# the hypothesis talks about the number of parties in the coalition, which is also mentioned in the premise
if parties_in_coalition_hypothesis != parties_in_coalition_premise:
    # check if the number of parties in the coalition in the hypothesis contradicts the number of parties from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

