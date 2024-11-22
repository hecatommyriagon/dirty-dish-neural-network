#!/bin/bash

if [[ -n "$VIRTUAL_ENV" ]]; then
    echo "Virtual environment is active: $VIRTUAL_ENV"
    echo "Creating kernel"
    pip install ipykernel
    ipython kernel install --user --name=projectname
    #python3 -m ipykernel install --user --name=.venv
    exit 0
else
    echo "No virtual environment is active."
    exit 1
fi
