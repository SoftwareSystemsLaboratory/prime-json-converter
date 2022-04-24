#!/bin/bash

rm -r dist
pip uninstall clime_json_converter -y
python -m build
pip install dist/clime_*

echo
echo "Done building"
