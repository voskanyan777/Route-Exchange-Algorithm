from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


from algorithm import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Укажите нужные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class EncodeMessage(BaseModel):
    user_input: str
    rows: int
    columns: int


@app.post('/encode-messages/')
async def encode_message(encoded_message: EncodeMessage):
    params = get_start_points(encoded_message.rows, encoded_message.columns)
    print(params)
    encode_message = encode(encoded_message.user_input, params, encoded_message.rows,
                            encoded_message.columns)
    return {
        'message': encode_message,
    }

@app.post('/decode-messages/')
async def decode_message(encoded_message: EncodeMessage):
    params = get_start_points(encoded_message.rows, encoded_message.columns)
    print(params)
    decode_message = decode(encoded_message.user_input, params, encoded_message.rows,
                            encoded_message.columns)

    return {
        'message': decode_message,
    }

@app.post('/original-encode-message')
async def original_encode_message(encoded_message: EncodeMessage):
    encode_message = original_encode(encoded_message.user_input, encoded_message.rows, encoded_message.columns)
    return {'message': encode_message}

@app.post('/original-decode-message')
async def original_decode_message(encoded_message: EncodeMessage):
    decode_message = original_decode(encoded_message.user_input, encoded_message.rows, encoded_message.columns)
    return {'message': decode_message}