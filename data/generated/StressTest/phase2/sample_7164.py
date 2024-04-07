# Premise: 15 people entered a theater before Sujit.
# Hypothesis: less than 65 people entered a theater before Sujit.
# Golden Label: entailment

people_before_sujit_premise = 15
people_before_sujit_hypothesis = 65

# the hypothesis talks about the number of people entering the theater before Sujit, also mentioned in the premise
if people_before_sujit_hypothesis <= people_before_sujit_premise:
    # check if the hypothesis value contradicts the information in the premise
    label = "contradiction"
elif people_before_sujit_hypothesis > people_before_sujit_premise:
    # the premise gives an exact number of people before Sujit
    # any number of people less than 'people_before_sujit_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

