# Test to Video Generator

Are you a small development team in a company?
Are your users requesting documentation on how to use your application?
Here is a a Python example on using tests to generate video example for your application.

- Browser automation with Playwright
- Text-to-speech with Piper-TTS

## Setup

```bash
# setup python env with uv
make
```

### Select browser

    playwright install

### Select voice

    python3 -m piper.download_voices | grep "DK"
    python3 -m piper.download_voices | grep "US"
    python3 -m piper.download_voices da_DK-talesyntese-medium
    python3 -m piper.download_voices en_US-amy-medium

## Run example





