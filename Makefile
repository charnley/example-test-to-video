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

# Run

dev-svelte:
	make -C ./services/web_application/ dev

record-molcalc:
	${python} -m playwright codegen https://molcalc.org

record-dev:
	${python} -m playwright codegen http://localhost:5173


# Admin

format:
	${python} -m pre_commit run --all-files

clean:
	rm videos/*.webm
