# define variables for the numerical entities in the input
pakistan_denies_india_claims = 1
india_pakistan_wars = 2
kashmir_possession = 3

# extract all quantities as valid numbers
pakistan_denies_india_claims = float(pakistan_denies_india_claims)
india_pakistan_wars = float(india_pakistan_wars)
kashmir_possession = float(kashmir_possession)

# compare the variables
if pakistan_denies_india_claims!= india_pakistan_wars:
    # check if the number of wars fought by Pakistan contradicts the number of wars mentioned in the premise
    label = "contradiction"
elif kashmir_possession!= 3:
    # check if the number of wars fought for the possession of Kashmir contradicts the number of wars mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
