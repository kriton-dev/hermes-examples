# Hermes examples

Convert PDFs to Markdown, extract text with OCR, transcribe audio, check websites and search public job boards with Apify Actors.
Each folder has a Python and curl example, its input and a real historical output; you pay per event when you run an Actor.

## Public Actors

These are the 26 Hermes Actors public in Apify Store on October 30, 2026; new ones are added as they publish.
The registry column lists the 12 active entries returned by the official MCP registry on the same date; a dash means no entry was returned.
Prices below are USD per named event at FREE / BRONZE, copied from the Actor manifests; other tiers appear under the detailed prices below.
An automatic start costs $0.00005 per started GB of run memory wherever “plus start” appears.
Requested prices are conditional, as described in the corresponding detailed price section; the run's actual active pricing record determines the bill.

### Files and media

| Actor | Job | Event prices (USD) | Apify MCP | Official MCP registry name |
| --- | --- | --- | --- | --- |
| [audio-to-transcript](https://apify.com/hermeskd/audio-to-transcript) | Transcribe audio and video, with optional speaker labels. | $0.006 / `audio-minute-transcribed`; $0.002 / `speaker-labelled-minute`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/audio-to-transcript) | — |
| [audio-video-convert](https://apify.com/hermeskd/audio-video-convert) | Convert audio and video files between formats. | $0.001 / `audio-minute-processed`; $0.022 / `video-minute-processed`; $0.045 / `hd-video-minute`; $0.008 / `low-resolution-video-minute`; $0.002 / `media-probed`; $0.001 / `file-copied`; $0.0005 / `copy-megabyte`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/audio-video-convert) | — |
| [document-to-markdown](https://apify.com/hermeskd/document-to-markdown) | Convert office documents and spreadsheets to Markdown. | $0.002 / `document-converted`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/document-to-markdown) | — |
| [file-downloader](https://apify.com/hermeskd/file-downloader) | Download public files from URLs into Apify storage. | $0.001 / `file-downloaded`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/file-downloader) | `io.github.kriton-dev/file-downloader` |
| [image-metadata-remover](https://apify.com/hermeskd/image-metadata-remover) | Remove image metadata such as EXIF and GPS. | $0.001 / `image-processed`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/image-metadata-remover) | — |
| [image-to-text](https://apify.com/hermeskd/image-to-text) | Extract text from images with OCR. | $0.002 / `image-ocr`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/image-to-text) | `io.github.kriton-dev/image-to-text` |
| [image-upscale](https://apify.com/hermeskd/image-upscale) | Upscale images with graphics and photo modes. | $0.0157 / `megapixel-upscaled`; $0.0144 / `photo-quarter-megapixel-restored`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/image-upscale) | — |
| [pdf-to-markdown](https://apify.com/hermeskd/pdf-to-markdown) | Convert PDF pages to Markdown and text, with OCR for scans. | $0.0005 / `pdf-page-converted`; $0.003 / `pdf-page-ocr`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/pdf-to-markdown) | `io.github.kriton-dev/pdf-to-markdown` |
| [video-frames](https://apify.com/hermeskd/video-frames) | Extract video frames by timestamp, interval or scene. | $0.001 / `frame-extracted`; $0.002 / `video-probed`; $0.015 / `minute-scanned`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/video-frames) | — |

### Website checks

| Actor | Job | Event prices (USD) | Apify MCP | Official MCP registry name |
| --- | --- | --- | --- | --- |
| [broken-links](https://apify.com/hermeskd/broken-links) | Check web pages for broken links. | $0.0005 / `link-checked`; $0.001 / `page-crawled`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/broken-links) | — |
| [dns-and-email-auth](https://apify.com/hermeskd/dns-and-email-auth) | Look up DNS records and check SPF, DKIM and DMARC. | $0.002 / `domain-checked`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/dns-and-email-auth) | `io.github.kriton-dev/dns-and-email-auth` |
| [domain-availability](https://apify.com/hermeskd/domain-availability) | Check domain registration through RDAP. | $0.001 / `domain-checked`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/domain-availability) | `io.github.kriton-dev/domain-availability` |
| [lighthouse-audit](https://apify.com/hermeskd/lighthouse-audit) | Measure Lighthouse performance, accessibility and SEO scores. | Requested schedule (conditional): $0.024 / `lighthouse-audit`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/lighthouse-audit) | — |
| [page-change-monitor](https://apify.com/hermeskd/page-change-monitor) | Compare a public page with a supplied previous snapshot. | $0.001 / `page-checked`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/page-change-monitor) | `io.github.kriton-dev/page-change-monitor` |
| [seo-page-audit](https://apify.com/hermeskd/seo-page-audit) | Audit on-page SEO, metadata, structured data and links. | $0.004 / `page-audited`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/seo-page-audit) | `io.github.kriton-dev/seo-page-audit` |
| [sitemap-urls](https://apify.com/hermeskd/sitemap-urls) | Extract URLs from sitemaps and sitemap indexes. | $0.0003 / `url-listed`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/sitemap-urls) | `io.github.kriton-dev/sitemap-urls` |
| [website-screenshot](https://apify.com/hermeskd/website-screenshot) | Capture web page screenshots and print pages to PDF. | Requested schedule (conditional): $0.0015 / `screenshot-captured`; $0.003 / `pdf-rendered`; $0.001 / `browser-started`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/website-screenshot) | — |
| [website-tech-stack](https://apify.com/hermeskd/website-tech-stack) | Detect technologies used by a public website. | $0.001 / `site-analyzed`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/website-tech-stack) | `io.github.kriton-dev/website-tech-stack` |

### Jobs

| Actor | Job | Event prices (USD) | Apify MCP | Official MCP registry name |
| --- | --- | --- | --- | --- |
| [ats-job-search](https://apify.com/hermeskd/ats-job-search) | Search job postings from verified public ATS boards. | $0.002 / `job-matched`; $0.01 / `search-run`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/ats-job-search) | `io.github.kriton-dev/ats-job-search` |
| [company-ats-board](https://apify.com/hermeskd/company-ats-board) | Find a company careers board and its public jobs. | $0.003 / `company-resolved`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/company-ats-board) | — |
| [greenhouse-jobs](https://apify.com/hermeskd/greenhouse-jobs) | Read public Greenhouse job board postings. | $0.001 / `job-returned`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/greenhouse-jobs) | — |
| [lever-jobs](https://apify.com/hermeskd/lever-jobs) | Read public Lever job postings. | $0.001 / `job-returned`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/lever-jobs) | — |
| [remote-jobs](https://apify.com/hermeskd/remote-jobs) | Read remote job postings from public feeds. | $0.001 / `job-returned`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/remote-jobs) | — |

### Data

| Actor | Job | Event prices (USD) | Apify MCP | Official MCP registry name |
| --- | --- | --- | --- | --- |
| [article-extractor](https://apify.com/hermeskd/article-extractor) | Extract article text and metadata from public web pages. | $0.001 / `article-extracted`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/article-extractor) | `io.github.kriton-dev/article-extractor` |
| [rss-feed-reader](https://apify.com/hermeskd/rss-feed-reader) | Read RSS, Atom and JSON feeds as structured records. | $0.001 / `feed-read`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/rss-feed-reader) | `io.github.kriton-dev/rss-feed-reader` |
| [url-to-markdown](https://apify.com/hermeskd/url-to-markdown) | Convert a public web page to Markdown for LLMs. | Requested schedule (conditional): $0.0015 / `page-converted`; $0.003 / `page-rendered`; plus start | [MCP](https://mcp.apify.com/?tools=hermeskd/url-to-markdown) | — |


## Call an Actor three ways

### 1. Apify API

Install Python 3.12 or later and the client with `python -m pip install -r requirements.txt`, or use Bash and curl.
Set `APIFY_TOKEN` in your environment through your own secret manager or shell; the examples never contain a credential.
From this directory, run `python pdf-to-markdown/example.py` or `bash pdf-to-markdown/example.sh`; replace the folder name with any Actor in the table.
Both scripts find `input.json` beside themselves, so they also work from another working directory.
The Python example starts the Actor, checks its terminal status and reads its dataset; the shell example uses the synchronous dataset API.
Both send the README's exact example input and maximum charge allowance, with a 300-second Actor timeout and a bounded client wait.
The synchronous API returns JSON dataset items; HTTP or run failures make the scripts exit unsuccessfully.
Calling these scripts runs a hosted Actor and can incur the listed event and start charges, capped by the example's maximum charge.

Each folder's `output.json` is the real historical example record copied verbatim from that Actor's README.
It is an example record, not a newly executed run or a promise that today's timestamps, URLs, artifacts or live jobs match it.
The scripts print the current dataset as a JSON array. Artifact links in historical output may expire.

### 2. Apify MCP server

Add the table's per-Actor MCP URL to an MCP client that supports streamable HTTP, and authenticate using your own Apify account.
For PDF conversion, use [the PDF MCP server](https://mcp.apify.com/?tools=hermeskd/pdf-to-markdown).
Call the exposed Actor tool with the contents of `pdf-to-markdown/input.json`.
For a server exposing the general `call-actor` tool, use this envelope:

```json
{
  "actor": "hermeskd/pdf-to-markdown",
  "input": {"urls": ["https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"], "includeText": true, "includeChunks": true},
  "callOptions": {"maxTotalChargeUsd": 0.05},
  "waitSecs": 45
}
```

If the tool returns a running job, use its run identifier to wait for completion, then `get-dataset-items` with the returned dataset identifier.
For another Actor, use its table MCP URL and its folder's `input.json`; its Apify page documents its own worked agent call.

### 3. Official MCP registry, where published

In a registry-aware MCP client, search for the exact registry name in the table, such as `io.github.kriton-dev/pdf-to-markdown`.
Install that entry's streamable HTTP remote, authenticate with Apify, then call the Actor with its folder's `input.json` as above.
The registry entry is a discovery route to the same Apify MCP service, with the same charges.
For an Actor with no registry entry, or a client that cannot install one, use the table's direct Apify MCP URL.

## Detailed prices and conditions

The following price sections are copied unchanged from each Actor README, including tier discounts, start charges, rounding and pending-price qualifications.
Consult the linked Actor page and the run's active pricing record before running an example.

### article-extractor

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `article-extracted` | Article extracted | One page fetched and its main text returned. | $0.001 | $0.0009 | $0.0008 |

Platform usage is not passed through. Apify's automatic actor-start event remains $0.00005 per started GB (one GB or less counts once). The synthetic dataset-item event is absent. Charge limits stop further paying work; unprocessed inputs receive uncharged errors. Completed readable pending events are settled on abort.

Worked cost example: ten successful article extracted events cost $0.01 at list, plus actor start. Failures are not included in that count.

### ats-job-search

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `job-matched` | Job matched | One matching posting returned. | $0.002 | $0.0018 | $0.0016 |
| `search-run` | Search run | One search across the directory (once per run). | $0.01 | $0.009 | $0.008 |

Worked cost: a search returning 25 jobs costs 25 × $0.002 + $0.01 = $0.06 at the FREE and BRONZE price, $0.054 on SILVER and $0.048 on GOLD and above, plus the actor-start event.

Platform usage is not passed through. Apify's automatic actor-start event remains $0.00005 per started GB (one GB or less counts once). The synthetic dataset-item event is absent. Failure records and the free summary records are never charged; when the run's maximum total charge is reached, further work stops and the rest gets uncharged `charge_limit_reached` records. Work completed before an abort is settled.

### audio-to-transcript

Pay per event; platform usage is included in the price, never passed through.

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `audio-minute-transcribed` | Audio minute transcribed | One started minute of media duration transcribed. | $0.006 | $0.0054 | $0.0048 |
| `speaker-labelled-minute` | Speaker-labelled minute | One started minute of media duration given speaker labels (only with speakerLabels: true, and only when a speaker is found). | $0.002 | $0.0018 | $0.0016 |

**When these prices start.** These prices are active now, since 2026-10-28 (1:38:02 AM US Central), as confirmed by this Actor’s public pricing record: $0.006 a minute and $0.002 more per minute when speaker labels are requested and a speaker is found. Both events took effect on the same date; the previous $0.008 a minute no longer applies to new runs. Apify normally schedules significant changes after 14 days, but an Actor with no paying users can change immediately. Speaker labels are available now and are never produced unpaid. A run whose own pricing lacks the label event transcribes and charges minutes only and explains the missing labels in `speakerLabelsUnavailable` and its status message. Word timestamps have no extra charge.

Apify also charges its standard `apify-actor-start` event: $0.00005 per GB of run memory (2 events, $0.0001, at the default 2,048 MB). The minimum maximum-charge a caller can set is $0.02.

Worked example on the FREE tier: a 30-minute podcast episode and a 45-second voice note cost 30 × $0.006 + 1 × $0.006 = $0.186, plus $0.0001 for the start, $0.1861 in all; with speaker labels add 31 × $0.002 = $0.062, $0.2481 in all. Word timestamps cost nothing extra. Minutes are counted from the media's duration, silence included; nothing is charged for a failed file.

### audio-video-convert

This is the **unprepared requested candidate**, not an active tariff or an accepted local stage. The actual active Apify pricing record controls charges. No activation date is established here. Shared preparation and monthly/notice validation must succeed before staging; publication and activation are separately gated.

The captured previous schedule, only while that exact record is active: audio $0.001/minute, standard $0.015/minute and HD $0.045/minute; new probe/copy/low events are unavailable. The requested schedule below applies only if the matching record is actually served. Platform usage is included, never passed through.

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `audio-minute-processed` | Audio minute processed | One started minute of input processed by an operation whose output is audio only. | $0.001 | $0.0009 | $0.0008 |
| `video-minute-processed` | Video minute processed | One started input minute for video or GIF output when neither the HD nor the qualified short low-resolution event applies. | $0.022 | $0.0198 | $0.0176 |
| `hd-video-minute` | HD video minute processed | One started minute of input processed by an operation whose output is video or GIF, when the output or the source video has more pixels than 1280x720 (720p); charged instead of video-minute-processed. | $0.045 | $0.0405 | $0.036 |
| `low-resolution-video-minute` | Qualified short low-resolution minute | One started minute for a qualified short transcode or exact trim: source and output fit 854x480, H.264 at most 24 fps, source at most 12 seconds and 16 MB, output at most 8 MB, 1024 MB allocation and at most 20 seconds work. Replaces the standard minute. | $0.008 | $0.0072 | $0.0064 |
| `media-probed` | Bounded technical media probe | One readable technical result: at most 16 MB input, 10 seconds download and inspection, 32 streams and 32 KiB result; at most 1024 MB allocation. No converted media artifact. | $0.002 | $0.0018 | $0.0016 |
| `file-copied` | Verified packet-copy trimmed file | One readable opt-in MP4 H.264 packet-copy trim with optional AAC, at most 1080p, 100000 packets, 1 GB input and output each, 120 seconds and 1024-4096 MB allocation. Also charges copy-megabyte, never processing minutes. | $0.001 | $0.0009 | $0.0008 |
| `copy-megabyte` | Combined packet-copy input and output MB | Each started decimal MB of downloaded input plus copied output, ceil((inputBytes + outputBytes) / 1000000), minimum one. Charged together with file-copied after readable delivery; never processing minutes. | $0.0005 | $0.00045 | $0.0004 |

Requested platform start: `apify-actor-start` $0.00005 per started GB of allocation in every tier (one at default 1,024 MB; four at 4,096 MB). It applies even if all files fail; failed files incur no processing events. Minimum maximum-charge setting is $0.05. A started encoding minute rounds up; probe/copy use their own units. The daily one-file batch retains `output-01.mp3`; single `url` retains `output.mp3`.

The lower standard and HD proposals were not selected: the conservative requested standard rate and unchanged HD rate above retain the enterprise stress basis. Long-480p discounting is not offered. All requested amounts remain conditional until the public pricing record proves them.

### broken-links

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `link-checked` | Link checked | One successful unique link or asset check, backed by a readable successful summary. | $0.0005 | $0.00045 | $0.0004 |
| `page-crawled` | Page crawled | One successfully fetched and parsed site page, backed by a readable successful summary. | $0.001 | $0.0009 | $0.0008 |

Platform usage is not passed through. Apify's automatic actor-start event remains $0.00005 per started GB (one GB or less counts once). The synthetic dataset-item event is absent. Charge limits stop further paying work; unprocessed inputs receive uncharged errors. Completed readable pending events are settled on abort.

Worked example: two successful unique checks and one 404 on one parsed page cost $0.002 at list ($0.001 for two checks plus $0.001 for the page), plus actor start. linksChecked is three; link-checked events are two. Duplicate checks, broken/error findings and failed/unreadable summaries add no events.

### company-ats-board

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `company-resolved` | Company resolved | One company matched to its hiring system and board. | $0.003 | $0.0027 | $0.0024 |

Worked cost: 40 companies of which 30 resolve cost 30 × $0.003 = $0.09 at the FREE and BRONZE price, $0.081 on SILVER and $0.072 on GOLD and above, plus the actor-start event.

Platform usage is not passed through. Apify's automatic actor-start event remains $0.00005 per started GB (one GB or less counts once). The synthetic dataset-item event is absent. Failure records and the free summary records are never charged; when the run's maximum total charge is reached, further work stops and the rest gets uncharged `charge_limit_reached` records. Work completed before an abort is settled.

### dns-and-email-auth

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `domain-checked` | Domain checked | One domain resolved and assessed successfully. | $0.002 | $0.0018 | $0.0016 |

Platform usage is not passed through. Apify's automatic actor-start event remains $0.00005 per started GB (one GB or less counts once). The synthetic dataset-item event is absent. Charge limits stop further paying work; unprocessed inputs receive uncharged errors. Completed readable pending events are settled on abort.

Worked cost example: ten successful primary events cost $0.02 at list, plus actor start. Failures are not included in that count.

### document-to-markdown

Pay per event; platform usage is included in the price, never passed through.

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `document-converted` | Document converted | One file converted to Markdown. | $0.002 | $0.0018 | $0.0016 |

Apify also charges its standard `apify-actor-start` event: $0.00005 per GB of run memory (2 events, $0.0001, at the default 2,048 MB). The minimum maximum-charge a caller can set is $0.01.

Worked example on the FREE tier: 10 files cost 10 × $0.002 = $0.02, plus $0.0001 for the start, $0.0201 in all. A file is one document whatever its length; nothing is charged for a failed file.

### domain-availability

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `domain-checked` | Domain checked | One domain answered available or registered. | $0.001 | $0.0009 | $0.0008 |

Platform usage is not passed through. Apify's automatic actor-start event remains $0.00005 per started GB (one GB or less counts once). The synthetic dataset-item event is absent. Charge limits stop further paying work; unprocessed inputs receive uncharged errors. Completed readable pending events are settled on abort.

Worked cost example: ten successful primary events cost $0.01 at list, plus actor start. Failures are not included in that count.

### file-downloader

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `file-downloaded` | File downloaded | One file fetched and saved to the run's key-value store. | $0.001 | $0.0009 | $0.0008 |

Platform usage is not passed through. Apify's automatic actor-start event remains $0.00005 per started GB (one GB or less counts once). The synthetic dataset-item event is absent. Charge limits stop further paying work; unprocessed inputs receive uncharged errors. Completed readable pending events are settled on abort.

Worked cost example: ten successful file downloaded events cost $0.01 at list, plus actor start. Failures are not included in that count.

### greenhouse-jobs

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `job-returned` | Job returned | One posting returned. | $0.001 | $0.0009 | $0.0008 |

Worked cost: five boards with 40 matching jobs each cost 200 × $0.001 = $0.20 at the FREE and BRONZE price, $0.18 on SILVER and $0.16 on GOLD and above, plus the actor-start event.

Platform usage is not passed through. Apify's automatic actor-start event remains $0.00005 per started GB (one GB or less counts once). The synthetic dataset-item event is absent. Failure records and the free summary records are never charged; when the run's maximum total charge is reached, further work stops and the rest gets uncharged `charge_limit_reached` records. Work completed before an abort is settled.

### image-metadata-remover

Pay per event; platform usage is included in the price, never passed through.

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `image-processed` | Image processed | One image cleaned and stored, or with reportOnly read and reported. | $0.001 | $0.0009 | $0.0008 |

One event per image, charged only after the cleaned file is stored (or the report written) and its record written; whatever the format, size and number of fields removed. Apify also charges its standard `apify-actor-start` event: $0.00005 per GB of run memory (1 event, $0.00005, at the default 1,024 MB). The minimum maximum-charge a caller can set is $0.01.

Worked example on the FREE tier: the photo above costs $0.001 plus $0.00005 for the start, $0.00105 in all; a run of 100 photos costs 100 × $0.001 = $0.10 plus the start. Nothing is charged for an image that fails.

### image-to-text

Pay per event; platform usage is included in the price, never passed through.

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `image-ocr` | Image read | One image read by OCR. | $0.002 | $0.0018 | $0.0016 |

Apify also charges its standard `apify-actor-start` event: $0.00005 per GB of run memory (4 events, $0.0002, at the default 4,096 MB). The minimum maximum-charge a caller can set is $0.01.

Worked example on the FREE tier: 10 screenshots cost 10 × $0.002 = $0.02, plus $0.0002 for the start, $0.0202 in all. Nothing is charged for a failed image.

### image-upscale

Pay per event; platform usage is included in the price, never passed through.

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `megapixel-upscaled` | Input megapixel upscaled | One started megapixel of input image upscaled. | $0.0157 | $0.01413 | $0.01256 |
| `photo-quarter-megapixel-restored` | Photo quarter-megapixel restored | One started quarter megapixel (250,000 pixels) of input photo restored and enlarged in mode photo. | $0.0144 | $0.01296 | $0.01152 |

Mode `graphics` is charged `megapixel-upscaled` per started megapixel of input — width × height / 1,000,000 rounded up, at least 1 — whatever the `scale` and `format`; mode `photo` is charged `photo-quarter-megapixel-restored` per started quarter megapixel — width × height / 250,000 rounded up, at least 1. Each is charged only after the file is stored and its record written. Apify also charges its standard `apify-actor-start` event: $0.00005 per GB of run memory (4 events, $0.0002, at the default 4,096 MB). The minimum maximum-charge a caller can set is $0.05.

Price change: the prices in the table and worked examples are active now, since 2026-10-28 (2:01:55 AM US Central), as confirmed by this Actor’s public pricing record. Graphics costs $0.0157 per started input megapixel and photo costs $0.0144 per started quarter megapixel; photo mode is available now. The previous graphics price of $0.01 no longer applies to new runs. Apify can apply a significant change immediately when an Actor has no paying users; a 14-day delay must not be assumed from the announcement date. Why the rise: on Apify a full-megapixel image runs about 50 seconds at the default memory (the model's measured time on Apify plus the run around it), which costs more than $0.01 earns; $0.0157 is the lowest price that covers it by 25% on every paying tier.

Photo mode per image against the lane's best-known photo upscaler (`danitn11/pisa-sr-image-upscaler`, its store prices read 2026-10-27: one price per image whatever its size, $0.02 FREE, $0.018 BRONZE, $0.015 SILVER, $0.012 GOLD and above, and its callers also pay the platform usage of each run, which this Actor never passes on):

- up to 0.25 MP (500 × 500): 1 photo event — this Actor $0.0144 FREE and BRONZE, $0.01296 SILVER, $0.01152 GOLD and above; that Actor $0.02 FREE, $0.018 BRONZE, $0.015 SILVER, $0.012 GOLD and above per image, plus platform usage.
- up to 0.5 MP (707 × 707): 2 photo events — this Actor $0.0288 FREE and BRONZE, $0.02592 SILVER, $0.02304 GOLD and above; that Actor $0.02 FREE, $0.018 BRONZE, $0.015 SILVER, $0.012 GOLD and above per image, plus platform usage.
- up to 1 MP (1000 × 1000): 4 photo events — this Actor $0.0576 FREE and BRONZE, $0.05184 SILVER, $0.04608 GOLD and above; that Actor $0.02 FREE, $0.018 BRONZE, $0.015 SILVER, $0.012 GOLD and above per image, plus platform usage.
- up to 2 MP (1414 × 1414): 8 photo events — this Actor $0.1152 FREE and BRONZE, $0.10368 SILVER, $0.09216 GOLD and above; that Actor $0.02 FREE, $0.018 BRONZE, $0.015 SILVER, $0.012 GOLD and above per image, plus platform usage.

This Actor is the cheaper of the two only for photos up to a quarter megapixel; above that it costs more per image, because its price follows the work (it runs on CPU, about 2 minutes per input megapixel). Its output is the input at 2x or 4x, the same price either way; that Actor's is a 1–2 megapixel target.

Worked examples on the FREE tier, at the new prices: the 480 × 360 photo above (0.17 megapixels) in mode `graphics` is 1 started megapixel, $0.0157, plus $0.0002 for the start, $0.0159 in all; in mode `photo` it is 1 started quarter megapixel, $0.0144 plus the start, $0.0146. Ten 1,600 × 1,200 images (1.92 megapixels each) in mode `graphics` are 2 started megapixels each, 10 × 2 × $0.0157 = $0.314 plus the start. Nothing is charged for a failed image.

### lever-jobs

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `job-returned` | Job returned | One posting returned. | $0.001 | $0.0009 | $0.0008 |

Worked cost: three sites with 50 matching postings each cost 150 × $0.001 = $0.15 at the FREE and BRONZE price, $0.135 on SILVER and $0.12 on GOLD and above, plus the actor-start event.

Platform usage is not passed through. Apify's automatic actor-start event remains $0.00005 per started GB (one GB or less counts once). The synthetic dataset-item event is absent. Failure records and the free summary records are never charged; when the run's maximum total charge is reached, further work stops and the rest gets uncharged `charge_limit_reached` records. Work completed before an abort is settled.

### lighthouse-audit

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `lighthouse-audit` | Lighthouse audit run | One successful URL audit for one form factor. | $0.024 | $0.0216 | $0.0192 |

The table shows the requested new prices. The previous rates apply until Apify makes the increase effective; the previous schedule is recorded in the Changelog. The run’s Apify pricing record determines its charge. Apify normally delays significant increases for 14 days and limits them to one per month; it can apply a change immediately when there are no paying users. No effective date has been confirmed for this increase.

Platform usage is not passed through. Apify's automatic actor-start event remains $0.00005 per started GB (one GB or less counts once). The synthetic dataset-item event is absent. Charge limits stop further paying work; unprocessed inputs receive uncharged errors. Completed readable pending events are settled on abort.

Worked cost example: at the requested price, ten successful audits cost $0.24 at list plus $0.0002 actor start at the default 4,096 MB, or $0.2402 in all. The previous-schedule total is recorded in the Changelog. Failures are not included in that count.

### page-change-monitor

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `page-checked` | Page checked | One page fetched and compared with its last snapshot. | $0.001 | $0.0009 | $0.0008 |

Platform usage is not passed through. Apify's automatic actor-start event remains $0.00005 per started GB (one GB or less counts once). The synthetic dataset-item event is absent. Charge limits stop further paying work; unprocessed inputs receive uncharged errors. Completed readable pending events are settled on abort.

Worked cost example: ten successful page checked events cost $0.01 at list, plus actor start. Failures are not included in that count.

### pdf-to-markdown

Pay per event; platform usage is included in the price, never passed through.

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `pdf-page-converted` | PDF page converted | One page converted from its text layer to Markdown. | $0.0005 | $0.00045 | $0.0004 |
| `pdf-page-ocr` | PDF page converted with OCR | One scanned page converted by OCR; charged instead of, not in addition to, pdf-page-converted. | $0.003 | $0.0027 | $0.0024 |

Apify also charges its standard `apify-actor-start` event: $0.00005 per GB of run memory (4 events, $0.0002, at the default 4,096 MB). The minimum maximum-charge a caller can set is $0.01.

Worked example at FREE: ten text pages cost `10 × pdf-page-converted + 4 × apify-actor-start`; ten scanned pages cost `10 × pdf-page-ocr + 4 × apify-actor-start`, with no text-conversion event in the second sum. Apply the FREE prices listed above; other tiers use their own column. Failed documents incur no page charge; the automatic start remains payable.

### Short PDFs, scans and per-file pricing

At the observed 2026-10-28 prices and default memory, a long text-only PDF costs more here than on [memo23/pdf-text-extractor](https://apify.com/memo23/pdf-text-extractor), which charges per document plus a start fee. For one file per run, this Actor is cheaper through nineteen text pages at list price, not for every text PDF. Short text PDFs and scans favor Hermes in that dated comparison.

The comparison includes each default-memory start, direct public downloads, no proxy fee and no tax. Volume, memory, tiers or later competitor prices change the comparison. This Actor never adds a chunk, upload or plain-text fee. The exact dated comparison arithmetic is retained in the build evidence; the checked event table and start total above determine this listing's prices.

### remote-jobs

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `job-returned` | Job returned | One posting returned. | $0.001 | $0.0009 | $0.0008 |

Worked cost: a search returning 50 listings costs 50 × $0.001 = $0.05 at the FREE and BRONZE price, $0.045 on SILVER and $0.04 on GOLD and above, plus the actor-start event.

Platform usage is not passed through. Apify's automatic actor-start event remains $0.00005 per started GB (one GB or less counts once). The synthetic dataset-item event is absent. Failure records and the free summary records are never charged; when the run's maximum total charge is reached, further work stops and the rest gets uncharged `charge_limit_reached` records. Work completed before an abort is settled.

### rss-feed-reader

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `feed-read` | Feed read | One feed fetched and its items returned. | $0.001 | $0.0009 | $0.0008 |

Platform usage is not passed through. Apify's automatic actor-start event remains $0.00005 per started GB (one GB or less counts once). The synthetic dataset-item event is absent. Charge limits stop further paying work; unprocessed inputs receive uncharged errors. Completed readable pending events are settled on abort.

Worked cost example: ten successful feed read events cost $0.01 at list, plus actor start. Failures are not included in that count.

### seo-page-audit

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `page-audited` | Page audited | One successfully fetched and audited HTML page. | $0.004 | $0.0036 | $0.0032 |

Platform usage is not passed through. Apify's automatic actor-start event remains $0.00005 per started GB (one GB or less counts once). The synthetic dataset-item event is absent. Charge limits stop further paying work; unprocessed inputs receive uncharged errors. Settlement of completed readable work is attempted on abort; interruption can leave a charge unconfirmed.

Worked cost example: ten successful primary events cost $0.04 at list, plus actor start. Failures are not included in that count.

### sitemap-urls

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `url-listed` | URL listed | One unique matching URL written from a sitemap. | $0.0003 | $0.00027 | $0.00024 |

Platform usage is not passed through. Apify's automatic actor-start event remains $0.00005 per started GB (one GB or less counts once). The synthetic dataset-item event is absent. Charge limits stop further paying work; unprocessed inputs receive uncharged errors. Completed readable pending events are settled on abort.

Worked cost example: ten successful primary events cost $0.003 at list, plus actor start. Failures are not included in that count.

### url-to-markdown

<!-- hermes-price-transition:v1 -->

The active Apify pricing record determines your bill; each schedule below is conditional on that exact record being active. A pending record does not authorise its charges. Before submission, while pending, and after activation, use the actual active record, not the requested calendar, to determine the bill.

Requested activation: 2026-11-13T00:00:00Z. This is a request until confirmed by the record; the record supplies the actual effective instant.

### Previous schedule — only if that record is active

`apify-actor-start`: FREE $0.00005, BRONZE $0.00005, SILVER $0.00005, GOLD $0.00005, PLATINUM $0.00005, DIAMOND $0.00005; `page-converted`: FREE $0.001, BRONZE $0.001, SILVER $0.0009, GOLD $0.0008, PLATINUM $0.0008, DIAMOND $0.0008; `page-rendered`: FREE $0.003, BRONZE $0.003, SILVER $0.0027, GOLD $0.0024, PLATINUM $0.0024, DIAMOND $0.0024.

### Requested schedule — only if that record is active

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `page-converted` | Page converted | One page fetched and converted without a browser. | $0.0015 | $0.00135 | $0.0012 |
| `page-rendered` | Page rendered and converted | One page rendered in a browser and converted; charged instead of page-converted. | $0.003 | $0.0027 | $0.0024 |

Platform event in the requested schedule: `apify-actor-start`: FREE $0.00005, BRONZE $0.00005, SILVER $0.00005, GOLD $0.00005, PLATINUM $0.00005, DIAMOND $0.00005.

The requested start at default memory is (1 event, $0.00005, at the default 1,024 MB).

Worked event subtotal, requested schedule at FREE: if 10 `page-converted` events are charged, 10 × $0.0015 = $0.015 for that event alone. All other charged events and the platform start event add their listed fees; this subtotal is not a run total. The configured maximum-charge floor is $0.01. Platform usage is included; failed results are uncharged.

<!-- /hermes-price-transition -->

### video-frames

Pay per event; platform usage is included in the price, never passed through.

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `frame-extracted` | Frame extracted | One still frame saved. | $0.001 | $0.0009 | $0.0008 |
| `video-probed` | Video probed | One video's metadata read. | $0.002 | $0.0018 | $0.0016 |
| `minute-scanned` | Minute scanned | One started minute of video decoded by the scene scan (scenes mode only). | $0.015 | $0.0135 | $0.012 |

All are charged after the video's record is written: `video-probed` once per video read, `frame-extracted` once per frame stored, and in `scenes` mode `minute-scanned` once per started minute of video the scene pass decoded (`minutesScanned` on the record; 52 seconds is one minute, 60.1 seconds two). `interval` and `timestamps` mode seek to each frame instead of decoding the video and charge no minutes. Apify also charges its standard `apify-actor-start` event: $0.00005 per GB of run memory (one event, $0.00005, at the default 1,024 MB). The minimum maximum-charge a caller can set is $0.02.

Worked example on the FREE tier, the minimal input under How to use it: one video probed ($0.002) and three frames ($0.003), plus $0.00005 for the start — $0.00505 in all. Ten videos with 20 frames each cost 10 × $0.002 + 200 × $0.001 = $0.22, plus the start. In `scenes` mode, a 9 min 56 s film with 40 scene changes is one video probed ($0.002), 10 minutes scanned ($0.15) and 40 frames ($0.04): $0.192, plus the start. Nothing is charged for a failed video.

### website-screenshot

<!-- hermes-price-transition:v1 -->

The active Apify pricing record determines your bill; each schedule below is conditional on that exact record being active. A pending record does not authorise its charges. Before submission, while pending, and after activation, use the actual active record, not the requested calendar, to determine the bill.

Requested activation: 2026-11-16T00:00:00Z. This is a request until confirmed by the record; the record supplies the actual effective instant.

### Previous schedule — only if that record is active

`apify-actor-start`: FREE $0.00005, BRONZE $0.00005, SILVER $0.00005, GOLD $0.00005, PLATINUM $0.00005, DIAMOND $0.00005; `screenshot-captured`: FREE $0.0015, BRONZE $0.0015, SILVER $0.00135, GOLD $0.0012, PLATINUM $0.0012, DIAMOND $0.0012; `pdf-rendered`: FREE $0.003, BRONZE $0.003, SILVER $0.0027, GOLD $0.0024, PLATINUM $0.0024, DIAMOND $0.0024.

- 1 screenshot in a run: 1 × 0.0015 + 0 + 0.00005 = $0.00155.
- 10 screenshots in a run: 10 × 0.0015 + 0 + 0.00005 = $0.01505, or $0.001505 each.
- Hypothetical 100-capture comparison (the input limit is 50): 100 × 0.0015 + 0 + 0.00005 = $0.15005, or $0.0015005 each.

For this schedule only, against an Actor at $0.00089 per screenshot plus usage at 4 GB and $0.20 per compute unit, this schedule is cheaper at more than 2.9700 seconds for one screenshot, 2.7675 seconds per screenshot for 10, or 2.7473 seconds per screenshot for 100 (hypothetical; the input limit is 50).

### Requested schedule — only if that record is active

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `screenshot-captured` | Screenshot captured | One image captured. | $0.0015 | $0.00135 | $0.0012 |
| `pdf-rendered` | Page printed to PDF | One page printed to PDF; charged instead of screenshot-captured. | $0.003 | $0.0027 | $0.0024 |
| `browser-started` | Browser started (once per run) | Once per run, with the run's first successful capture: starting the browser on Apify's servers. Not charged when no capture succeeds. | $0.001 | $0.0009 | $0.0008 |

- 1 screenshot in a run: 1 × 0.0015 + 0.001 + 0.00005 = $0.00255.
- 10 screenshots in a run: 10 × 0.0015 + 0.001 + 0.00005 = $0.01605, or $0.001605 each.
- Hypothetical 100-capture comparison (the input limit is 50): 100 × 0.0015 + 0.001 + 0.00005 = $0.15105, or $0.0015105 each.

For this schedule only, against an Actor at $0.00089 per screenshot plus usage at 4 GB and $0.20 per compute unit, this schedule is cheaper at more than 7.4701 seconds for one screenshot, 3.2175 seconds per screenshot for 10, or 2.7923 seconds per screenshot for 100 (hypothetical; the input limit is 50).

Platform event in the requested schedule: `apify-actor-start`: FREE $0.00005, BRONZE $0.00005, SILVER $0.00005, GOLD $0.00005, PLATINUM $0.00005, DIAMOND $0.00005.

The requested start at default memory is (1 event, $0.00005, at the default 1,024 MB).

Worked event subtotal, requested schedule at FREE: if 10 `screenshot-captured` events are charged, 10 × $0.0015 = $0.015 for that event alone. All other charged events and the platform start event add their listed fees; this subtotal is not a run total. The configured maximum-charge floor is $0.01. Platform usage is included; failed results are uncharged.

<!-- /hermes-price-transition -->

### website-tech-stack

| Event | Title | Charged when | FREE / BRONZE | SILVER | GOLD / PLATINUM / DIAMOND |
|---|---|---|---|---|---|
| `site-analyzed` | Site analyzed | One page fetched and its technologies returned. | $0.001 | $0.0009 | $0.0008 |

Platform usage is not passed through. Apify's automatic actor-start event remains $0.00005 per started GB (one GB or less counts once). The synthetic dataset-item event is absent. Charge limits stop further paying work; unprocessed inputs receive uncharged errors. Completed readable pending events are settled on abort.

Worked cost example: ten successful site analyzed events cost $0.01 at list, plus actor start. Failures are not included in that count.
