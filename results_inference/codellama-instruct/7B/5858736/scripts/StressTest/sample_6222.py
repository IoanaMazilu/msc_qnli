# define variables for the numerical entities in the premise and hypothesis
premise_mani_share = 200
premise_rani_share = 200
hypothesis_mani_share = 400
hypothesis_rani_share = 400

# compare the variables to determine if the hypothesis is entailed from the premise
if hypothesis_mani_share - premise_mani_share <= 0 and hypothesis_rani_share - premise_rani_share <= 0:
    label = "entailment"
elif hypothesis_mani_share - premise_mani_share > 0 or hypothesis_rani_share - premise_rani_share > 0:
    label = "contradiction"
else:
    label = "neutral"

print(label)
