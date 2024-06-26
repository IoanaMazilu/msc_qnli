dimes_premise_melanie = 7.0
dimes_given_dad = 8.0
dimes_given_mom = 4.0
total_dimes_premise = dimes_premise_melanie + dimes_given_dad + dimes_given_mom

if total_dimes_premise - dimes_given_dad - dimes_given_mom!= 5.0:
    label = "contradiction"
else:
    label = "entailment"

print(label)
