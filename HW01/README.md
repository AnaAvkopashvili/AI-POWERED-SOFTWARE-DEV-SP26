### Evaluation


In almost every questions I have provided both models answered pretty much the same way (same outputs) including match problems which is considered as soft spot for LLMs
The question I find in Reddit was breaking point for those models:

 
`A snail climbs a 10-meter pole. Each day it climbs 3 meters, each night it slides back 2 meters.
However, on rainy days (every 3rd day starting from day 1), it only climbs 1 meter and slides back 3 meters at night.
How many days does it take to reach the top? Show your work step by step.`

The answer for this question was that snail never reaches the top with given conditions, gemini-2.5-flash provided that answer
with only 85 in / 1110 out tokens, while gemini-2.5-flash-lite keep Hallucinating, insists that snail reaches to on Dat 100, consumed Way more tokens
and burned money with no clear solution:  85 in / 24223 out

Here is cost summary:

[gemini-2.5-flash]

  • Token usage: 85 in / 1110 out (total 6584)

  • Response time: 27375.7 ms

  • Estimated cost: $0.002801



[gemini-2.5-flash-lite]

  • Token usage: 85 in / 24223 out (total 24308)

  • Response time: 39989.3 ms

  • Estimated cost: $0.009698






