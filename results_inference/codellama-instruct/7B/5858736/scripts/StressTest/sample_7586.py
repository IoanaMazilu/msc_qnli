king_code = 17
don_code = 18
mass_code = 37

if king_code == 17 and don_code == 18:
    # check if the hypothesis values contradict the premise
    if mass_code == 37:
        label = "entailment"
    else:
        label = "contradiction"
else:
    label = "neutral"

print(label)
