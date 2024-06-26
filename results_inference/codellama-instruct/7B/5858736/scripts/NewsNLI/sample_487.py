premise_members = 3
hypothesis_members = 2

# the hypothesis mentions two anti-war members of Congress, which is less than the three mentioned in the premise
if hypothesis_members < premise_members:
    label = "contradiction"
else:
    label = "neutral"

print(label)
