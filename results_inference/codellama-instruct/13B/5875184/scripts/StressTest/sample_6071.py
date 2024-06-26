premise = "The 2 nd builder builds in 15 days, then how many 2's are used by the builder from Chennai in numbering the 100 homes?"
hypothesis = "The more than 2 nd builder builds in 15 days, then how many 2's are used by the builder from Chennai in numbering the 100 homes?"

# extract the numerical entities from the premise and hypothesis
premise_days = 15
premise_builders = 2
premise_homes = 100

hypothesis_days = 15
hypothesis_builders = 2
hypothesis_homes = 100

# compare the numerical entities
if premise_builders == hypothesis_builders and premise_days == hypothesis_days and premise_homes == hypothesis_homes:
    # the hypothesis is a direct entailment of the premise
    label = "entailment"
elif premise_builders == hypothesis_builders and premise_days == hypothesis_days and premise_homes > hypothesis_homes:
    # the hypothesis is a contradiction to the premise
    label = "contradiction"
else:
    # the hypothesis is neutral to the premise
    label = "neutral"

print(label)
