# define variables with representative names for the numerical entities in both inputs
premise_gov_parties = "CDA, VVD, D66"
hypothesis_gov_parties = "CDA, VVD, D66"

# extract all quantities as valid numbers (integers or floats)
premise_gov_parties_list = premise_gov_parties.split(",")
hypothesis_gov_parties_list = hypothesis_gov_parties.split(",")

# use brief comments to explain what comparison you do between the defined variables
# do not use their values in the comments

# compare the number of parties in the premise and hypothesis
if len(premise_gov_parties_list)!= len(hypothesis_gov_parties_list):
    # if the number of parties in the hypothesis does not match the number of parties in the premise, it is a contradiction
    label = "contradiction"
elif len(premise_gov_parties_list) == len(hypothesis_gov_parties_list):
    # if the number of parties in the hypothesis matches the number of parties in the premise, we need to check if the parties are the same
    for party in premise_gov_parties_list:
        if party not in hypothesis_gov_parties_list:
            # if there is at least one party in the hypothesis that is not in the premise, it is a contradiction
            label = "contradiction"
            break
    else:
        # if all parties in the hypothesis are also in the premise, we can infer entailment
        label = "entailment"

print(label)
