#!/usr/bin/env bash

# Builds the files for distribution and uploads them to PyPI, provided that:
#   - You are on the main branch and there are no uncommitted changes.
#   - All the style checks run without errors.
#   - All the tests run with errors.
#
# By default, the script uploads to Test PyPI (test.pypi.org); to upload to the real PyPI, run with
# the argument -r.
#
# In either case, you will be asked for username and password. The username should be __token__,
# while the password is the token generated by PyPI for the account.

set -euf

UPLOAD_TO_REAL_PYPI=false

while getopts 'r' c; do
  case "${c}" in
    r)
      UPLOAD_TO_REAL_PYPI=true
      ;;
  esac
done

BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [[ "${BRANCH}" != "main" ]]; then
  echo "You can only publish from the main branch, but you are currently on '${BRANCH}'."
  exit 1;
fi

if [ "$(git status --porcelain)" ]; then
  echo "You have uncommitted changes. Clean them up before publishing."
  exit 1;
fi

bash build.sh
if [ "${UPLOAD_TO_REAL_PYPI}" == true ]; then
  echo ""
  echo "=== Publishing package to the real PyPI ==="
  python3 -m twine upload dist/*
else
  echo "Publishing to test"
  python3 -m twine upload --repository testpypi dist/*
fi
