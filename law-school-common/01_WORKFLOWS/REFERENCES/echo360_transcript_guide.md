# Echo360 Login Guide

# Guide: How to Download Echo360 Transcripts

This document provides step-by-step instructions for navigating to Echo360, finding a specific class lecture, and downloading the transcript.

### Authentication Details

### 1. How to Get to the Website (Authentication)

This guide provides the exact steps and commands used to log into Echo360 using browser automation tools.

### Prerequisites

1. A file named `cookie for echo360` located at `/Users/mosheklein/Documents/Projects/law school projects/_system_tools/misc/`.
2. This file must contain two key pieces of information:
   * The target URL for the Echo360 content page.
   * The full, valid cookie string for your session.

### Step 1: Navigate to the Echo360 URL

The first step is to open a browser and navigate to the target URL. This will initially redirect to a login page.

**Tool Used:** `mcp7_browser_navigate`

```json
{
  "url": "https://echo360.org/content#userIdentifier=833c9952-2b46-4562-b268-f64c26b9db50_a30bf2d3-ebf0-4b5e-8279-a7e38f3228c3"
}
```

### Step 2: Set Session Cookies

While on the login page, execute a series of JavaScript commands to set the necessary session cookies. Each part of the cookie string is set individually. This is done by wrapping the `document.cookie` assignment in a function and passing it to the `mcp7_browser_evaluate` tool.

**Tool Used:** `mcp7_browser_evaluate`

```json
// Command 1
{
  "function": "() => { document.cookie = 'ECHO_JWT=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJFY2hvMzYwLkF1dGhuIiwic3ViIjoibWs1MTcwQGNvbHVtYmlhLmVkdSIsImV4cCI6MTc2MDg2MjUwMywiaWF0IjoxNzYwODE1NzAzLCJqdGkiOiI0MjA2ZGJmMS01MDg3LTQyZjctYWYxOC0xZjhlMDY4OTkxMmIiLCJjb250ZW50Ijp7InNlc3Npb25JZCI6IjQyZWU0ZjdkLWIyM2YtNGMxOC04MmY3LWU4ZGIwMjEyZThjZSIsInVzZXJJZCI6IjgzM2M5OTUyLTJiNDYtNDU2Mi1iMjY4LWY2NGMyNmI5ZGI1MCIsImluc3RpdHV0aW9uSWQiOiJhMzBiZjJkMy1lYmYwLTRiNWUtODI3OS1hN2UzOGYzMjI4YzMiLCJkb21haW4iOiJlY2hvMzYwLm9yZyIsImtleUlkIjoiZTE4NGM4MjUtMjc1OC00ZmQwLWI1MWMtNGQyZmY2NWE5ZTNlIiwic3NvSWQiOiJtazUxNzBAY29sdW1iaWEuZWR1IiwicnFyb2xlIjoic3R1ZGVudCJ9fQ.dKKlYXUOBdkJDgNcZxq_T2FLH7w8Vf8NxRNH98pgdHk; path=/; domain=.echo360.org;'; }"
}

// Command 2
{
  "function": "() => { document.cookie = 'CloudFront-Tracking2=MTc2MDgxOTMwNDA1OOKQn+KQn+KQn+KQn2EzMGJmMmQzLWViZjAtNGI1ZS04Mjc5LWE3ZTM4ZjMyMjhjM+KQn+KQn+KQn+KQny5lY2hvMzYwLm9yZ+KQn+KQny8; path=/; domain=.echo360.org;'; }"
}

// Command 3
{
  "function": "() => { document.cookie = 'PLAY_SESSION=93b9dd7513db31cc6d6dee032c155a4b8da6dc8a-role=Student&institution=a30bf2d3-ebf0-4b5e-8279-a7e38f3228c3&authn=true&roles=Student&csrfToken=63beb964ea1a4cc034d93808035d520f750aa51a-1760815703535-e1da533513ca4a84a40014bf&sessionExpiresAt=2025-10-18T23%3A28%3A23.514Z&user=833c9952-2b46-4562-b268-f64c26b9db50&sessionCode=42ee4f7d-b23f-4c18-82f7-e8db0212e8ce; path=/; domain=.echo360.org;'; }"
}

// Command 4
{
  "function": "() => { document.cookie = 'CloudFront-Key-Pair-Id=APKAIPMYRDQXV3PXG2XA; path=/; domain=.echo360.org;'; }"
}

// Command 5
{
  "function": "() => { document.cookie = 'CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vKi5lY2hvMzYwLm9yZy8qYTMwYmYyZDMtZWJmMC00YjVlLTgyNzktYTdlMzhmMzIyOGMzLyoiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjA4MjI5MDR9fX1dfQ__; path=/; domain=.echo360.org;'; }"
}

// Command 6
{
  "function": "() => { document.cookie = 'CloudFront-Signature=mQu5e9ZetADy-Gvc3HMp8wMt9Fd9fWTvTNFhSCS~OyYo-UIycuxwudQc0eOMOmWEkm9hdQfV1j5AwYEGf-5z4azdFgNREIXO9TM2o9mESuSSHtFaAjGyZk8xJvwqbtzpNWcC~ShX2qSYSSSVlGadEcqQNkKlg90TD0IDIjopOu2psTs2DiZe42sNiLYVj5LVvkwWmbtDn1Baw7Ok4v9xen0dsO4YwJ-akSDKYMXbqHRpoZDFe23n-2JhjQxaQFNgM-6OKtfNSmVciCcYRYOGCGGm1nLbgxYn8cPZMHClkH9axirTplspEPHWcS0mheXsQ9uWQn3k0xmfHmrXDtwVkA__; path=/; domain=.echo360.org;'; }"
}
```

### Step 3: Reload the Page

After all the cookies have been set, navigate to the target URL again. This reloads the page, and the browser will now send the session cookies with the request, resulting in a successful login.

**Tool Used:** `mcp7_browser_navigate`

```json
{
  "url": "https://echo360.org/content#userIdentifier=833c9952-2b46-4562-b268-f64c26b9db50_a30bf2d3-ebf0-4b5e-8279-a7e38f3228c3"
}
```

This completes the login process.

### 2. How to Go to a Class

Once logged in, you can navigate to the desired course.

- **Tool Used:** `mcp-playwright`
- **Process:**
  1. Click the "Courses" link in the main navigation bar (`mcp7_browser_click`).
  2. From the list of courses, identify the correct one (e.g., "Constitutional Law," "Civil Procedure"). Note that lecture recordings are typically in the "Restricted" folder.
  3. Click on the link for the correct course.

### 3. How to Find the Right Date

Finding the correct lecture requires paying attention to the date.

- **Logic:**
  1. Use the current date as a reference point.
  2. Identify the most recent lecture date that has already passed.
  3. Be aware that lectures listed with future dates are placeholders and will not have content.

### 4. How to Download the Transcript

Once you've opened the correct lecture:

- **Tool Used:** `mcp-playwright`
- **Process:**
  1. Click the "Transcripts panel" button to open the transcript view.
  2. Click the "download transcripts" button.
  3. In the download dialog, click the button for "Plain Text Format File" (`.txt`).

### 5. What to Do with the Downloaded Transcript

After downloading, the transcript file needs to be saved to the appropriate location.

- **Process:**
  1. The downloaded file will be in a temporary directory (e.g., `/var/folders/...`).
  2. Read the content of this temporary file using the `read_file` tool.
  3. Save the content to a permanent file in the appropriate course folder (e.g., `law_school_projects/transcripts/conlaw/lecture_date.txt`).

### 6. File Renaming

This file has been renamed from `cookie for echo360` to `echo360_transcript_guide.md` to better reflect its purpose.

### 7. Tools Used

The following tools from the `mcp-playwright` server were essential for this task:

- `mcp7_browser_navigate`
- `mcp7_browser_click`
- `mcp7_browser_evaluate`
- `mcp7_browser_snapshot`

Other tools used:

- `read_file`
- `write_to_file`
- `replace_file_content`
