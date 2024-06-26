accused_people_premise = 1000
victims_hypothesis = 2

# The hypothesis mentions that at least two people have died from drinking the hallucinogenic potion
# The premise also mentions that around 1000 people were forced to drink the potion, but there is no information on the number of deaths

if victims_hypothesis > accused_people_premise:
    # If the number of victims in the hypothesis is greater than the number of accused people in the premise, it's a contradiction
    label = "contradiction"
else:
    # If not, it's neutral because the premise does not provide information on the number of deaths
    label = "neutral"

print(label)
