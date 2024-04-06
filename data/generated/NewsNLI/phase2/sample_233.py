# Premise: Federer secured the winning point in his singles match against Fabio Fognini to give Switzerland an unbeatable 3-1 lead over Italy in Geneva.
# Hypothesis: Gives Swiss an unbeatable 3-1 lead in tie against Italy.
# Golden Label: entailment

lead_premise = 3.1
lead_hypothesis = 3.1

# the hypothesis mentions the unbeatable lead of Switzerland over Italy, which is also referenced in the premise
# however, the hypothesis does not specify who gives the lead, which was specified in the premise by Federer
if lead_hypothesis != lead_premise:
    # check if the lead in the hypothesis contradicts the lead reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer neutrality, since not all information from the premise is mentioned in the hypothesis
    label = "neutral"

print(label)

