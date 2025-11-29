GIT_ROOT:=$(shell git rev-parse --show-toplevel)

env=env
python=${env}/bin/python

all: ${env} voices browsers

# Setup

${env}:
	uv venv ${env} --python 3.12
	uv pip install -r requirements.txt --python ./${env}/bin/python
	uv pip install -e . --python ./${env}/bin/python

voices:
	mkdir $@
	${python} -m piper.download_voices en_US-amy-medium --download-dir ./voices

browsers:
	echo $@

# Run

example:
	${python} -m ${package} --args

test:
	${python} -m pytest ./tests/

types:
	${python} -m monkeytype run `which pytest` ./tests/
	${python} -m monkeytype list-modules | grep ${package} | xargs -n1 monkeytype apply
