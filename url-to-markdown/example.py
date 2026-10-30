"""Run the documented url-to-markdown example. Requires APIFY_TOKEN."""

import json
import os
from datetime import timedelta
from decimal import Decimal
from pathlib import Path

from apify_client import ApifyClient


def main():
    token = os.environ.get('APIFY_TOKEN')
    if not token:
        raise SystemExit('Set APIFY_TOKEN in your environment before running this example.')
    run_input = json.loads(Path(__file__).with_name('input.json').read_text(encoding='utf-8'))
    client = ApifyClient(token)
    run = client.actor('hermeskd/url-to-markdown').call(
        run_input=run_input,
        max_total_charge_usd=Decimal('0.05'),
        run_timeout=timedelta(seconds=300),
        wait_duration=timedelta(seconds=360),
        timeout=360,
    )
    if run is None or run.get('status') != 'SUCCEEDED':
        raise SystemExit('The Actor did not succeed; inspect the run in Apify Console.')
    print(json.dumps(list(client.dataset(run['defaultDatasetId']).iterate_items(timeout=60)), indent=2))


if __name__ == '__main__':
    main()
