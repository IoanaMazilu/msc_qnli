# Premise: (CNN) -- A North Carolina man's decision to put tattoos on his two dogs is drawing yelps of criticism and wagging tails of support across social media.
# Hypothesis: North Carolina man put intricate tattoos on his two dogs.
# Golden Label: entailment

dogs_premise = 2
dogs_hypothesis = 2

# the hypothesis mentions the number of dogs that the man in North Carolina tattooed, which is also mentioned in the premise
# it also states that the tattoos are intricate, but this cannot be entailed from the premise
label = "neutral"

print(label)

