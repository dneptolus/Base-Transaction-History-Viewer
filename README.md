# Base Transaction History Viewer

## Description

**Base Transaction History Viewer** is a simple and intuitive service that allows users to view the transaction history of any wallet on the Base blockchain. By entering a wallet address, users can retrieve and display all associated transactions in a user-friendly interface.

## Technologies

- **Python**: Backend logic and blockchain interaction via Web3.py
- **Flask**: Web framework for creating the web interface
- **Web3.py**: Library for interacting with EVM-compatible blockchains
- **Requests**: Handling HTTP requests to external APIs
- **HTML/CSS**: Creating a simple and clean user interface

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/base-transaction-history-viewer.git
    cd base-transaction-history-viewer
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure RPC URL and API:**

    - Create a `.env` file in the root directory:

        ```bash
        touch .env
        ```

    - Add your RPC URL to the `.env` file:

        ```plaintext
        BASE_RPC_URL=https://base-mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID
        ```

    - **Note:** Replace `YOUR_INFURA_PROJECT_ID` with your actual Infura project ID or another RPC URL provider for Base.

5. **Run the application:**

    ```bash
    python app.py
    ```

6. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

## Usage

1. Enter a Base wallet address in the input field.
2. Click the "View Transactions" button.
3. View the transaction history displayed in a table format.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or suggestions, contact me at [your email] or open an issue in the repository.
