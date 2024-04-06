# Premise: (CNN) -- Four separate times, prosecutors say, Gregory Peterson lured women under the pretext of a movie or lunch -- and sexually assaulted them.
# Hypothesis: Four women allege he assaulted them.
# Golden Label: entailment

assault_cases_premise = 4
assault_cases_hypothesis = 4

# the hypothesis mentions the number of assault cases, which is also mentioned in the premise
if assault_cases_hypothesis != assault_cases_premise:
    # check if the number of assault cases in the hypothesis contradicts the number of assault cases reported in the premise
    label = "contradiction"
else:
    # if the number of assault cases in the hypothesis does not contradict the number of assault cases in the premise, we can infer entailment
    label = "entailment"

print(label)

