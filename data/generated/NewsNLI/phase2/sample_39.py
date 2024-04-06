# Premise: Lance Armstrong's appearance in Paisley, Scotland, saw around 200 people joining him on a bike ride.
# Hypothesis: A group of 200 people gathered in Paisley High Street to ride with Armstrong.
# Golden Label: entailment

people_premise = 200
people_hypothesis = 200

# the hypothesis mentions the number of people riding with Armstrong, which is also referenced in the premise
# however, the exact location within Paisley is specified differently in the hypothesis, which cannot be entailed from the premise
label = "neutral"

print(label)

