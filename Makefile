GIT_ROOT:=$(shell git rev-parse --show-toplevel)

env=env
python=./services/video_service/${env}/bin/python

all: envs voices browsers

# Setup

envs:
	make -C ./services/video_service/
	make -C ./services/web_application/

voices:
	mkdir $@
	${python} -m piper.download_voices en_US-amy-medium --download-dir ./voices

browsers:
	mkdir browsers
	${python} -m playwright install

example:
	${python} ./services/video_service/src/example.py

# Run

dev-svelte:
	make -C ./services/web_application/ dev

record:
	${python} -m playwright codegen http://localhost:5173


# Admin

clean:
	rm videos/*.webm
