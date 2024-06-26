corporate_percentage_premise = 70
corporate_percentage_hypothesis = 70
banking_percentage_premise = 20
banking_percentage_hypothesis = 20
usa_headquarters_percentage_premise = 60
usa_headquarters_percentage_hypothesis = 60

# the hypothesis talks about the sales structure of X & co, also mentioned in the premise
if corporate_percentage_hypothesis < corporate_percentage_premise:
    # check if the hypothesis value contradicts the estimate of 'corporate_percentage_premise'
    label = "contradiction"
elif banking_percentage_hypothesis != banking_percentage_premise:
    # check if the banking percentage in the hypothesis contradicts the banking percentage reported in the premise
    label = "contradiction"
elif usa_headquarters_percentage_hypothesis != usa_headquarters_percentage_premise:
    # check if the USA headquarters percentage in the hypothesis contradicts the USA headquarters percentage reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of corporate customers and their distribution
    # any percentage greater or equal to 'corporate_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
