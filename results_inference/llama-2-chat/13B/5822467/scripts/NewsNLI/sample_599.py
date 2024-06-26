women_premise = 2
dogs_premise = 2
house_premise = 1
waters_premise = 1

women_hypothesis = 2
dogs_hypothesis = 2
house_hypothesis = 1
waters_hypothesis = 1

# the hypothesis mentions the number of women and dogs trapped inside a house, which is also mentioned in the premise
# however, the hypothesis does not mention the flood waters or the foundation of the house, which are crucial details in the premise
label = "neutral"

print(label)
