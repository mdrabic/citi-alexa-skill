# Citibank Alexa Skill
Create a proof of concept that demonstrates:
 * Authenticate with users Citi account via OAuth
 * Combine multiple data points into one response such as summarizing all accounts
 * Convey basic data about a users account such as balance and payment due date
 * Demo conversational context

## Build

run `./build.py`. A zip will produced in the `out` folder that can be uploaded to AWS Lambda.

## Citi Sandbox Test Users

| Username      | Password    |
|    ---        |      ---    |
| SandboxUser1  | P@ssUser1$  |
| SandboxUser2  | P@ssUser2$  |
| SandboxUser3  | P@ssUser3$  |
| SandboxUser4  | P@ssUser4$  |

## Interactions
The planned voice interactions for the poc

### Brief me on my accounts
 You currently have <slot> credit card account(s) with a total outstanding balance of 
 <slot>. _iterate over each card_. For your account ending in <slot>, your outstanding balance is <slot> with a 
 remaining credit of <slot>. The next payment is due on <slot>. 


### List my accounts
 You currently have <slot> credit card account(s). _iterate over each product name and last four of 
 account number_
 
 
### What is the balance on my account ending in <slot>
You have an outstanding balance of <slot>.


### What is the balance on my account
_No account was provided so give the opportunity to demo conversational aspect of alexa. Alexa will respond with 
for which account?_

The user can respond with the account number or say I don't know my accounts? and Alexa can respond with "you have the 
following accounts..., "


### List my most recent transactions.
_Another conversational based flow. Alexa responds with "for which account?", etc_ 
