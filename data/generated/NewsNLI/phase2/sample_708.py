# Premise: (CNN) -- Around 1,000 people accused of being witches in Gambia have been locked up in secret detention centers and forced to drink a dangerous hallucinogenic potion, according to human rights organization Amnesty International.
# Hypothesis: Victims forced to drink dangerous hallucinogenic potion ; at least two have died.
# Golden Label: neutral

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

