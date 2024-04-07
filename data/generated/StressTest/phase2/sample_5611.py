# Premise: Cindy's mother gives her $more than 20 to spend.
# Hypothesis: Cindy's mother gives her $30 to spend.
# Golden Label: neutral

money_given_premise = 20
money_given_hypothesis = 30

# the hypothesis talks about the amount of money given to Cindy, also mentioned in the premise
if money_given_hypothesis <= money_given_premise:
    # check if the hypothesis value contradicts the premise's estimate of more than 'money_given_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money given
    # any amount of money greater than 'money_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

