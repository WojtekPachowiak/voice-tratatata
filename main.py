from typing import Optional
import typer
from schema import *
from audio import Tratatata, LetterToPhoneMap
app = typer.Typer()


@app.command()
def main(
        path: Optional[str] = typer.Argument(..., help="Path to a custom letter-phone map file. If left empty, the default dynamically-generated map will be used.")
    ):
    # a = AudioProcessing.parse_file("./audio_processing/a.json")
    # print(a)
    # dic = r"""
    # {
    #     "general": [
    #         {
    #             "type": "uniform",
    #             "value": "5"
    #         },
    #         {
    #             "type" : "a",
    #             "value" : "222",

    #         }
    #     ]
    # }
    # """
    # print(AudioProcessing( general=[Pitch(type="uniform", value=3)] ).json())
    l2p_map = LetterToPhoneMap()
    tratata = Tratatata(l2p_map)
    tratata.say("Hello world!")



if __name__ == "__main__":
    app()