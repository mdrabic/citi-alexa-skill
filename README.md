# Citibank Alexa Skill
Create a proof of concept that demonstrates:
 * Authenticate with users Citi account via OAuth
 * Combine multiple data points into one response such as summarizing all accounts
 * Convey basic data about a users account such as balance and payment due date
 * Achieve conversational context ie, ask "when is the bill due for my account ending in 1234" 
   a follow up question of "How much do I owe" will return the amount for account 1234. 

## Build

run `./build.py`. A zip will produced in the `out` folder that can be uploaded to AWS Lambda.

## Citi Sandbox Test Users

| Username      | Password    |
|    ---        |      ---    |
| SandboxUser1  | P@ssUser1$  |
| SandboxUser2  | P@ssUser2$  |
| SandboxUser3  | P@ssUser3$  |
| SandboxUser4  | P@ssUser4$  |