# Premise: And goods from the EU represent 16% of all Russian imports, EU numbers show.
# Hypothesis: Russia gets 16% of all its imports from the European Union.
# Golden Label: entailment

eu_imports_premise = 0.16
eu_imports_hypothesis = 0.16

# the hypothesis mentions the percentage of Russian imports from the EU, which is also mentioned in the premise
if eu_imports_hypothesis != eu_imports_premise:
    # check if the percentage of EU imports in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)

