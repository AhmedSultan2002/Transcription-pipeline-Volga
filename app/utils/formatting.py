def format_transcription_segments(raw_segments) -> list:
    """
    Transforms raw Whisper model output into a structured JSON schema 
    with timestamps and text segments.
    """
    structured_payload = []
    
    for segment in raw_segments:
        structured_payload.append({
            "start_time": round(segment.start, 2),
            "end_time": round(segment.end, 2),
            "segment_text": segment.text.strip(),
            "confidence": round(segment.avg_logprob, 2) 
        })
        
    return structured_payload