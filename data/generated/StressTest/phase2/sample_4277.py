# Premise: If Michael earned $352 last week, how many hours did he work?
# Hypothesis: If Michael earned $652 last week, how many hours did he work?
# Golden Label: contradiction

earnings_premise = 352
earnings_hypothesis = 652

# the hypothesis talks about the earnings of Michael, referenced also in the premise
if earnings_hypothesis == earnings_premise:
    # check if the earnings in the hypothesis contradicts the earnings reported in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are about the same individual and situation
    # but the numerical values mentioned are different, therefore, it's neutral
    label = "neutral"

print(label)

