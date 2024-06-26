bonds_denominations_premise = 70 or 100
bonds_denominations_hypothesis = 50 or 100

# the hypothesis talks about the denominations of bonds, which is also mentioned in the premise
if bonds_denominations_hypothesis!= bonds_denominations_premise:
    # if the denominations of bonds in the hypothesis are not the same as in the premise, it's a contradiction
    label = "contradiction"
else:
    # if the denominations of bonds are the same, it's a neutral statement
    label = "neutral"

print(label)
