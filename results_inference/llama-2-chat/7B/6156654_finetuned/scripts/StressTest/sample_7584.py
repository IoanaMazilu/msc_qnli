king_code = 17
don_code = 18

# the hypothesis refers to the same codes as the premise, but with different conditions
if king_code < 27 and don_code == 18:
    # the hypothesis conditions do not entail the premise condition
    label = "neutral"
elif king_code == 27 or don_code!= 18:
    # the hypothesis conditions contradict the premise condition
    label = "contradiction"
else:
    # the premise condition is true, but the hypothesis conditions are not relevant
    label = "entailment"

print(label)
