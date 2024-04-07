# Premise: How many days will it take both of them to complete the entire job, given that it would have taken David less than 52 days to complete the job alone?
# Hypothesis: How many days will it take both of them to complete the entire job, given that it would have taken David 12 days to complete the job alone?
# Golden Label: neutral

days_alone_premise = 52
days_alone_hypothesis = 12

# the hypothesis talks about the number of days David would take to complete the job alone, referenced also in the premise
if days_alone_hypothesis >= days_alone_premise:
    # check if the hypothesis value contradicts the estimate of less than 'days_alone_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days less than 'days_alone_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

