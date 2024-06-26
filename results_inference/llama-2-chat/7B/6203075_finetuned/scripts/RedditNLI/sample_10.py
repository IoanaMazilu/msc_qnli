rupee_premise = 65.36 / USD
rupee_hypothesis = 68.19 / USD
sensex_premise = 300
sensex_hypothesis = 282.50
nifty_premise = 27
nifty_hypothesis = 28

# the hypothesis talks about the current rupee value and the fall in Sensex and Nifty, which are also mentioned in the premise
if rupee_hypothesis!= rupee_premise:
    # check if the rupee value in the hypothesis contradicts the rupee value in the premise
    label = "contradiction"
elif sensex_hypothesis!= sensex_premise or nifty_hypothesis!= nifty_premise:
    # check if the fall in Sensex or Nifty in the hypothesis contradicts the fall in Sensex or Nifty in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
