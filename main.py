from typing import Optional
import typer
from audio import Tratatata

app = typer.Typer()


@app.command()
def main(
        output_path: Optional[str] = typer.Option(..., help="Path to the output file. If left empty, the output will be not be saved."),
        play_to_speakers: Optional[bool] = typer.Option(False, help="If True, the output will be played to speakers. If False, the output will not be played to speakers."),
        l2pm_path: Optional[str] = typer.Option(None, help="Path to a custom letter-phone map file. If left empty, the default map will be used."),
        gapm_path: Optional[str] = typer.Option(None, help="Path to a custom global audio processing map file. If left empty, the default map will be used."),
        sapm_path: Optional[str] = typer.Option(None, help="Path to a specific audio processing map file. If left empty, no specific audio processing will be used."),
    ):

    tratata = Tratatata(letter_to_phone_map = l2pm_path, global_audio_processing_map = gapm_path, specific_audio_processing_map = sapm_path)
    tratata.say("Hello world!", output_path = output_path, play_to_speakers = False)



if __name__ == "__main__":
    app()