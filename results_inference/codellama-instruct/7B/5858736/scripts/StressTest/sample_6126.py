iceland_visitors_premise = 31
norway_visitors_premise = 31
neither_country_visitors_hypothesis = 41

# the hypothesis talks about the number of people who have visited neither country, referenced also in the premise
if neither_country_visitors_hypothesis <= (iceland_visitors_premise + norway_visitors_premise):
    # check if the hypothesis value contradicts the estimate of less than 'neither_country_visitors_hypothesis'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who have visited both Iceland and Norway
    # any number of people greater than 'neither_country_visitors_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
