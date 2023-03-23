import typer
from schema import *

app = typer.Typer()

@app.command()
def main(
        path: str = typer.Argument(..., help="Path to the mapping file")
    ):
    a = AudioProcessing.parse_file("./audio_processing/a.json")
    print(a)
    dic = r"""
    {
        "general": [
            {
                "type": "uniform",
                "value": "5"
            },
            {
                "type" : "a",
                "value" : "222",

            }
        ]
    }
    """
    print(AudioProcessing( general=[Pitch(type="uniform", value=3)] ).json())



if __name__ == "__main__":
    app()