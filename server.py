from typing import Annotated

from fastapi import FastAPI, Response, Query
from tts import tts

app = FastAPI()


@app.get("/generate")
def generate(
    text: Annotated[
        str,
        Query(
            openapi_examples={
                "ru_1": {
                    "value": "Съешьте ещё этих мягких французских булочек, да выпейте чаю."
                },
                "ru_2": {
                    "value": "В недрах тундры выдры в гетрах тырят в вёдра ядра кедров."
                },
                "en_1": {
                    "value": "Can you can a canned can into an un-canned can like a canner can can a canned can into an un-canned can?"
                },
            },
        ),
    ],
    speaker: Annotated[
        str,
        Query(
            openapi_examples={
                "ru_aidar": {"value": "aidar"},
                "ru_baya": {"value": "baya"},
                "en_0": {"value": "en_0"},
            }
        ),
    ],
    sample_rate: Annotated[
        int,
        Query(
            openapi_examples={
                "8 000": {"value": 8_000},
                "24 000": {"value": 24_000},
                "48 000": {"value": 48_000},
            }
        )
        ] = 48_000,
):
    audio = tts.generate(text, speaker, sample_rate)
    return Response(audio, media_type="audio/wav")



@app.get("/speakers")
def speakers():
    return tts.speakers


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
