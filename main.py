from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Go to /bfhl"}


@app.get("/bfhl")
async def bfhl_get():
    return {
        "operation_code": 1
    }

@app.post("/bfhl")
async def bfhl_post(data: list):
    numbers = []
    alphabets = []
    maximum_alpha = ''

    if(len(data) > 0):
        for ele in data:
            if(ele.isdigit()):
                numbers.append(str(ele))
            elif(ele.isalpha()):
                if(maximum_alpha < ele.lower() or maximum_alpha == ''):
                    maximum_alpha = ele
                alphabets.append(str(ele))
            
    if maximum_alpha == '': 
        maximum_alpha = []
    else:
        maximum_alpha = [ maximum_alpha ]

    return {
        "is_success": True,
        "user_id": "maitrey_bhute_01042003", 
        "email" : "maitrey.bhute2020@vitstudent.ac.in",
        "roll_number":"20BCE0771",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_alphabet": maximum_alpha
    }