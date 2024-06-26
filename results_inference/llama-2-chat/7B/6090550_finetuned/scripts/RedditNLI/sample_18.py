# The hypothesis and premise both mention the Sensex and Nifty
sensex_pts_premise = 362.75
sensex_pts_hypothesis = 357.39
nifty_pts_hypothesis = 0 # No information in the premise about the Nifty points

# The hypothesis mentions a future trading call, which is not present in the premise
future_call_hypothesis = True

# The premise mentions a future trading call, which is also mentioned in the hypothesis
future_call_premise = False

# The hypothesis also mentions the India best advisory company, which is not present in the premise
advisory_company_hypothesis = False

# The premise does not mention any contradiction, so we infer neutrality
label = "neutral"

print(label)
