from faster_whisper import WhisperModel
import os

# Initialize the model at the module level so it loads into memory 
# only once upon startup, not every time the function is called.
transcription_model = WhisperModel("base", device="cpu", compute_type="int8")

def execute_transcription(file_path: str):
    """
    Core transcription service. Isolated from the web/API layer.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found at {file_path}")

    # Perform the transcription. 
    # Returns an iterator of segments and model info.
    segments, info = transcription_model.transcribe(
        file_path, 
        beam_size=5,
        vad_filter=True # Added for basic safety against silence
    )
    
    # Returning the raw iterator directly. 
    return segments, info