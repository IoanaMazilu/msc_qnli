# Premise: More young American adults live with parents than with partners or in other situations since 1880s.
# Hypothesis: For First Time In 130 Years, More Young Adults Live With Parents Than With Partners.
# Golden Label: entailment

year_premise = 1880
year_hypothesis = 130

# the hypothesis and premise mention a period of time from which the current situation has been changing
if year_hypothesis != 2021-year_premise:
    # check if the years in the hypothesis contradicts the years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

