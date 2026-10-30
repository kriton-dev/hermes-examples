#!/usr/bin/env bash
# Run the documented remote-jobs example. Requires APIFY_TOKEN.
set -euo pipefail
: "${APIFY_TOKEN:?Set APIFY_TOKEN in your environment before running this example.}"
example_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
curl --fail-with-body --silent --show-error \
  --connect-timeout 30 --max-time 360 \
  --request POST \
  --header "Authorization: Bearer $APIFY_TOKEN" \
  --header 'Content-Type: application/json' \
  --data-binary "@$example_dir/input.json" \
  'https://api.apify.com/v2/acts/hermeskd~remote-jobs/run-sync-get-dataset-items?timeout=300&maxTotalChargeUsd=0.05'
