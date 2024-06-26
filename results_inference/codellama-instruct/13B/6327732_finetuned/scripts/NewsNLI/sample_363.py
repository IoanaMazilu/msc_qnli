# define variables for the entities in the premise and hypothesis
premise_virus = "Stuxnet"
premise_facility = "Iran's Natanz nuclear facility"
hypothesis_virus = "Stuxnet virus"
hypothesis_facility = "Iran's Natanz nuclear facility"

# check if the hypothesis mentions the same virus and facility as the premise
if hypothesis_virus == premise_virus and hypothesis_facility == premise_facility:
    # if the hypothesis mentions the same virus and facility, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis does not mention the same virus and facility, we can infer neutrality
    label = "neutral"

print(label)
