import pandas
import datetime
import numpy
from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.post("/")
async def chat_bot(username:Optional[str] = Form(None), password:Optional[str] = Form(None), sensor_id: int = Form(...), tanggal:Optional[str] = Form(None)):
    if username == "twiscode" and password == "twiscode":
        total = 0
        df = pandas.read_csv("202009020838.csv", sep = ",")
        df['timestamp'] = df['timestamp'].apply(lambda x: pandas.Timestamp(x).strftime('%Y-%m-%d'))
        df['timestamp'] = pandas.to_datetime(df['timestamp'])
        hasil = df[df["sensor_id"] == int(sensor_id)]
        if tanggal:
            hasil = (hasil[hasil["timestamp"] == tanggal])
        print (hasil)
        for col in hasil['total']:
            total += int(col)
        return {
            "pesan": "berhasil login",
            "sensor_id": sensor_id,
            "tanggal": tanggal,
            "hasil": total,
        }
    else :
        return {
            "pesan": "gagal login"
        }
