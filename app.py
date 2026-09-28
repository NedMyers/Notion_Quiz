import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def run_my_script():
    # --- PASTE YOUR EXISTING SCRIPT LOGIC HERE ---
    result = "Hello from my Python script!"
    # --- END OF YOUR SCRIPT LOGIC ---
    return result

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
