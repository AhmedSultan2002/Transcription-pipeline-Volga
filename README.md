# Audio Transcription Pipeline

A robust, modular transcription service that accepts audio files and converts spoken language into text with segment-level timestamps. This pipeline leverages `faster-whisper` for memory-efficient speech-to-text processing and `pydub` (via `ffmpeg`) for universal audio format handling.

## Part 1: Implementation

### Prerequisites
- Python 3.8+
- `ffmpeg` installed on your host machine (required by `pydub` to decode various audio and video formats).

### Installation

1. Clone the repository and navigate into the project directory.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
