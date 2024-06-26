rake_travel_premise = 8800
rake_travel_hypothesis = 1800

# the hypothesis talks about the distance travelled by Rakesh, which is also mentioned in the premise
if rake_travel_hypothesis >= rake_travel_premise:
    # check if the hypothesis value contradicts the estimate of less than 'rake_travel_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance travelled
    # any distance less than 'rake_travel_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
