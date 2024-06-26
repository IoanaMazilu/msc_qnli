# Define variables for the numerical entities in the premise and hypothesis
premise_parties = 25
premise_candidate = "Madhav Kumar Nepal"

hypothesis_party = "Communist Party of Nepal (Unified Marxist-Leninist)"
hypothesis_candidate = "Nepal"

# Extract all quantities as valid numbers
premise_parties = int(premise_parties)
hypothesis_party = int(hypothesis_party)

# Check if the hypothesis candidate received backing from more than 20 of the 25 parties in parliament
if hypothesis_party > 20:
    label = "entailment"
else:
    label = "contradiction"

print(label)
