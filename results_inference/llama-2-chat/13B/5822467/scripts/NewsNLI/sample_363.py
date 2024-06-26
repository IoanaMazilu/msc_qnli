virus_premise = "Stuxnet virus"
facility_premise = "Natanz nuclear facility"
attack_hypothesis = "one such attack by Stuxnet virus"

# define variables with representative names for the numerical entities in both inputs
virus_hypothesis = "Stuxnet virus"
facility_hypothesis = "Natanz nuclear facility"

# extract all quantities as valid numbers (integers or floats)
virus_premise_int = int(virus_premise)
facility_premise_int = int(facility_premise)
attack_hypothesis_int = int(attack_hypothesis)

# use brief comments to explain what comparison you do between the defined variables
# do not use their values in the comments

# compare the variables
if attack_hypothesis_int == facility_premise_int:
    # the hypothesis mentions the same entity as the premise, but with a different description
    label = "neutral"
elif attack_hypothesis_int!= facility_premise_int:
    # the hypothesis mentions a different entity or a different description of the same entity
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
