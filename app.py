from flask import Flask, render_template, request
from web3 import Web3
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Get RPC URL from environment variables
BASE_RPC_URL = os.getenv("BASE_RPC_URL")

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(BASE_RPC_URL))

# Etherscan-like API for Base (replace with actual API if available)
BASE_API_URL = "https://api-base.blockchainexplorer.com/api"

@app.route('/', methods=['GET', 'POST'])
def index():
    transactions = []
    error = None
    if request.method == 'POST':
        address = request.form.get('address')
        if web3.isAddress(address):
            try:
                # Fetch transaction history using an API
                # Note: Replace BASE_API_URL with the actual API endpoint for Base blockchain
                response = requests.get(f"{BASE_API_URL}/account/{address}/transactions")
                if response.status_code == 200:
                    data = response.json()
                    transactions = data.get('transactions', [])
                else:
                    error = "Unable to fetch transaction history. Please try again later."
            except Exception as e:
                error = f"Error fetching transaction history: {str(e)}"
        else:
            error = "Invalid wallet address."
    return render_template('index.html', transactions=transactions, error=error)

if __name__ == '__main__':
    app.run(debug=True)
