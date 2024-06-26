# Define variables for the numerical entities in the premise and hypothesis
premise_vikas_rank = 7
premise_tanvi_rank = 17
hypothesis_vikas_rank = 9
hypothesis_tanvi_rank = 17

# Check if the hypothesis values contradict the premise values
if hypothesis_vikas_rank <= premise_vikas_rank:
    label = "contradiction"
elif hypothesis_tanvi_rank!= premise_tanvi_rank:
    label = "contradiction"
else:
    label = "entailment"

print(label)
