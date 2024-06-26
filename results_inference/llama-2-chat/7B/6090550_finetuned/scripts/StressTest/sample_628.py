y = 70

# the hypothesis states John has 10 pairs of matched socks, which is less than the number mentioned in the premise
if y > 10:
    # if the number of pairs of socks in the hypothesis is greater than the number in the premise, it contradicts the premise
    label = "contradiction"
elif y < 10:
    # if the number of pairs of socks in the hypothesis is less than the number in the premise, it cannot be fully entailed from the premise
    label = "neutral"
else:
    # if the number of pairs of socks in the hypothesis is equal to the number in the premise, it can be fully entailed from the premise
    label = "entailment"

print(label)
