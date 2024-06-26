# The premise mentions the death toll of 3 people in Damaturu, while the hypothesis mentions the death toll of 32 in Madalla
# We need to compare the death toll mentioned in the premise with the death toll mentioned in the hypothesis

if damaturu_death_toll == 32:
    # If the death toll in Damaturu is the same as the death toll in Madalla, then it is an entailment
    label = "entailment"
elif damaturu_death_toll!= 32:
    # If the death toll in Damaturu is not the same as the death toll in Madalla, then it is a contradiction
    label = "contradiction"
else:
    # If the death toll in Damaturu is the same as the death toll in Madalla, then it is neutral
    label = "neutral"

print(label)
