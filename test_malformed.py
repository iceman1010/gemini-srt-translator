#!/usr/bin/env python3
"""Test script to reproduce the malformed object error with a small SRT file."""
from dotenv import load_dotenv
load_dotenv()

import gemini_srt_translator as gst

gst.target_language = "German"
gst.input_file = "error_examples/test_malformed.srt"
gst.skip_upgrade = True

gst.translate()
