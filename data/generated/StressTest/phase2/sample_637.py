# Premise: If Michael earned $less than 720 last week, how many hours did he work?
# Hypothesis: If Michael earned $320 last week, how many hours did he work?
# Golden Label: neutral

earnings_premise = 720
earnings_hypothesis = 320

# the hypothesis refers to the earnings of Michael mentioned in the premise
if earnings_hypothesis >= earnings_premise:
    # check if the earnings in the hypothesis contradict the premise that earnings were less than 'earnings_premise'
    label = "contradiction"
else:
    # if the hypothesis earnings do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
