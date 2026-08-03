#!/usr/bin/env bash
set -euo pipefail

# How to run:
# bash browse_tsbow_offline.sh
# bash browse_tsbow_offline.sh 8080

PORT="${1:-8000}"
HTML_FILE="index.html"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
URL="http://localhost:${PORT}/${HTML_FILE}"

cd "${ROOT_DIR}"

if command -v python3 >/dev/null 2>&1; then
  PYTHON_CMD="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_CMD="python"
else
  echo "Error: python3 or python is required to start the local server." >&2
  exit 1
fi

if [[ ! -f "${HTML_FILE}" ]]; then
  echo "Error: ${HTML_FILE} was not found in ${ROOT_DIR}." >&2
  exit 1
fi

echo "Starting local server at http://localhost:${PORT}/"
"${PYTHON_CMD}" -m http.server "${PORT}" &
SERVER_PID=$!

cleanup() {
  kill "${SERVER_PID}" >/dev/null 2>&1 || true
}
trap cleanup EXIT INT TERM

sleep 1

echo "Open this URL in your browser: ${URL}"
echo "Server is running. Press Ctrl+C to stop."
wait "${SERVER_PID}"
