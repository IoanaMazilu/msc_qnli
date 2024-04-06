# Premise: Four babies have died from melamine-tainted infant formula and more than 52,000 children have fallen ill, Chinese authorities say.
# Hypothesis: Four infants in China dead, over 52,000 reported ill from tainted milk powder.
# Golden Label: entailment

death_premise = 4
death_hypothesis = 4
ill_premise = 52000
ill_hypothesis = 52000

# the hypothesis mentions the number of deaths and the number of children falling ill, which are also mentioned in the premise
if death_hypothesis != death_premise:
    # check if the number of deaths in the hypothesis contradicts the number of deaths reported in the premise
    label = "contradiction"
elif ill_hypothesis != ill_premise:
    # check if the number of ill children from the hypothesis contradicts the number of ill children in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

