country_premise = "Denmark"
country_hypothesis = "Sweden"

# check if the hypothesis contradicts the premise
if country_hypothesis!= country_premise:
    label = "contradiction"
else:
    # if the hypothesis and premise match, we can infer entailment
    label = "entailment"

print(label)
