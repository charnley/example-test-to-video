GIT_ROOT:=$(shell git rev-parse --show-toplevel)

env=env
python=${env}/bin/python

all: ${env} voices browsers

# Setup

${env}:
	uv venv ${env} --python 3.12
	uv pip install -r requirements.txt --python ./${env}/bin/python
	uv pip install -e . --python ./${env}/bin/python

node_modules:
	pnpm i

voices:
	mkdir $@
	${python} -m piper.download_voices en_US-amy-medium --download-dir ./voices

browsers:
	playwright install

# Run

dev-svelte:
	npm run dev

record:
	${python} -m playwright codegen http://localhost:5173

