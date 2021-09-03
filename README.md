# FibBank
Simple service solution  for a code challenge.


Tests

✅ Reset state before starting tests
POST /reset
Expected: 200 OK
Got:      200 OK

✅ Get balance for non-existing account
GET /balance?account_id=1234
Expected: 404 0
Got:      404 0

✅ Create account with initial balance
POST /event {"type":"deposit", "destination":"100", "amount":10}
Expected: 201 {"destination": {"id":"100", "balance":10}}
Got:      201 {"destination": {"id": "100", "balance": 10}}

✅ Deposit into existing account
POST /event {"type":"deposit", "destination":"100", "amount":10}
Expected: 201 {"destination": {"id":"100", "balance":20}}
Got:      201 {"destination": {"id": "100", "balance": 20}}

✅ Get balance for existing account
GET /balance?account_id=100
Expected: 200 20
Got:      200 20

✅ Withdraw from non-existing account
POST /event {"type":"withdraw", "origin":"200", "amount":10}
Expected: 404 0
Got:      404 0

✅ Withdraw from existing account
POST /event {"type":"withdraw", "origin":"100", "amount":5}
Expected: 201 {"origin": {"id":"100", "balance":15}}
Got:      201 {"origin": {"id": "100", "balance": 15}}

✅ Transfer from existing account
POST /event {"type":"transfer", "origin":"100", "amount":15, "destination":"300"}
Expected: 201 {"origin": {"id":"100", "balance":0}, "destination": {"id":"300", "balance":15}}
Got:      201 {"origin": {"id": "100", "balance": 0}, "destination": {"id": "300", "balance": 15}}

✅ Transfer from non-existing account
POST /event {"type":"transfer", "origin":"200", "amount":15, "destination":"300"}
Expected: 404 0
Got:      404 0


## Getting Started
The source is a Pycharm project

### Prerequisites

Python 3.8 and Flask

## Authors

Luciano Cardoso https://github.com/cardocha

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

