 Dawson_premise = 38
 Dawson_hypothesis = 68

 # the hypothesis refers to the time taken by Dawson to run the first leg of the course
 if Dawson_hypothesis <= Dawson_premise:
     # check if the hypothesis value contradicts the estimate of 'Dawson_premise'
     label = "contradiction"
 else:
     # the premise gives only an estimate for the time taken by Dawson
     # any time greater than 'Dawson_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
     label = "neutral"

 print(label)
