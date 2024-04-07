# Premise: Let Raj be less than 7 years older than Ravi and Hema be two years younger than Ravi.
# Hypothesis: Let Raj be 3 years older than Ravi and Hema be two years younger than Ravi.
# Golden Label: neutral

raj_older_than_ravi_premise = 7
raj_older_than_ravi_hypothesis = 3

hema_younger_than_ravi_premise = 2
hema_younger_than_ravi_hypothesis = 2

# The hypothesis talks about the age difference between Raj, Ravi and Hema, which is also mentioned in the premise
if raj_older_than_ravi_hypothesis > raj_older_than_ravi_premise:
    # check if the hypothesis value contradicts the premise estimate of Raj being less than 'raj_older_than_ravi_premise' years older than Ravi
    label = "contradiction"
elif hema_younger_than_ravi_hypothesis != hema_younger_than_ravi_premise:
    # check if the age difference of Hema and Ravi in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones and are less or equal, we can infer entailment
    label = "entailment"

print(label)

