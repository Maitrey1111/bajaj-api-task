from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Go to /bfhl"}

@app.route('/bfhl', methods=['GET', 'POST'])
async def handle_request():
    return {
        "status": 'True',
        "id": 12,
        "email": "1@gmail.com",
        "rollno": "20BCE0771",
        "numbers": [], 
        "alphabets": []
# 7. Highest Alphabet in the input array of alphabets [Refer to note in Annexure for more info]
    }