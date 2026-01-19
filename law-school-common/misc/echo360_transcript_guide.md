# Guide: How to Download Echo360 Transcripts

This document provides step-by-step instructions for navigating to Echo360, finding a specific class lecture, and downloading the transcript.

## Current Status

**✅ FULLY WORKING - VERIFIED ON OCTOBER 18, 2025:**

- Authentication (logging in with cookies)
- Navigating to courses page
- Selecting a course
- Opening a specific lecture/recording
- **Finding and downloading the transcript** (Successfully tested!)

**📝 NOTES:**

- Some lectures may not have a download button for the transcript if:
  - The lecture has not happened yet (future date)
  - The lecture happened too recently and the transcript isn't published yet
  - There was a technical issue with transcript generation
- The transcript download button is accessible through the player controls after clicking the "transcripts" button

### Authentication Details

The authentication cookies are stored in the file: `/Users/mosheklein/Documents/Projects/law school projects/_system_tools/misc/cookie for echo360`

**CRITICAL:** The cookies have an expiration time. If login fails, you will need to get fresh cookies from the user.

### 1. How to Get to the Website (Authentication)

**Step 1.1: Read the Cookie File**

Use `read_file` tool to get the URL and cookie string.

```
Tool: read_file
Parameters:
  file_path: /Users/mosheklein/Documents/Projects/law school projects/_system_tools/misc/cookie for echo360
```

The file contains:

- Line 1: The specific lesson URL (optional)
- Line 2: The content/library URL
- Line 3: Empty line
- Line 4: The full cookie string (all cookies separated by semicolons)

**Step 1.2: Navigate to the URL**

IMPORTANT: You MUST navigate to the login page FIRST before setting cookies. Do NOT navigate directly to the authenticated page.

```
Tool: mcp7_browser_navigate
Parameters:
  url: https://echo360.org/content#userIdentifier=833c9952-2b46-4562-b268-f64c26b9db50_a30bf2d3-ebf0-4b5e-8279-a7e38f3228c3
```

This will redirect you to a login page at: `https://login.echo360.org/login?appId=...`

**Step 1.3: Set the Cookies**

CRITICAL SYNTAX: The cookie-setting JavaScript MUST be wrapped in an arrow function: `() => { ... }`

You need to set 6 cookies in total. Parse the cookie string from line 4 and split it by `"; "` to get individual cookies.

For EACH cookie, use:

```
Tool: mcp7_browser_evaluate
Parameters:
  function: () => { document.cookie = 'COOKIE_NAME=COOKIE_VALUE; path=/; domain=.echo360.org;'; }
```

The 6 cookies to set (in order):

1. **ECHO_JWT cookie:**

```
Tool: mcp7_browser_evaluate
Parameters:
  function: () => { document.cookie = 'ECHO_JWT=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJFY2hvMzYwLkF1dGhuIiwic3ViIjoibWs1MTcwQGNvbHVtYmlhLmVkdSIsImV4cCI6MTc2MDg2MjUwMywiaWF0IjoxNzYwODE1NzAzLCJqdGkiOiI0MjA2ZGJmMS01MDg3LTQyZjctYWYxOC0xZjhlMDY4OTkxMmIiLCJjb250ZW50Ijp7InNlc3Npb25JZCI6IjQyZWU0ZjdkLWIyM2YtNGMxOC04MmY3LWU4ZGIwMjEyZThjZSIsInVzZXJJZCI6IjgzM2M5OTUyLTJiNDYtNDU2Mi1iMjY4LWY2NGMyNmI5ZGI1MCIsImluc3RpdHV0aW9uSWQiOiJhMzBiZjJkMy1lYmYwLTRiNWUtODI3OS1hN2UzOGYzMjI4YzMiLCJkb21haW4iOiJlY2hvMzYwLm9yZyIsImtleUlkIjoiZTE4NGM4MjUtMjc1OC00ZmQwLWI1MWMtNGQyZmY2NWE5ZTNlIiwic3NvSWQiOiJtazUxNzBAY29sdW1iaWEuZWR1IiwicnFyb2xlIjoic3R1ZGVudCJ9fQ.dKKlYXUOBdkJDgNcZxq_T2FLH7w8Vf8NxRNH98pgdHk; path=/; domain=.echo360.org;'; }
```

2. **CloudFront-Tracking2 cookie:**

```
Tool: mcp7_browser_evaluate
Parameters:
  function: () => { document.cookie = 'CloudFront-Tracking2=MTc2MDgxOTMwNDA1OOKQn+KQn+KQn+KQn2EzMGJmMmQzLWViZjAtNGI1ZS04Mjc5LWE3ZTM4ZjMyMjhjM+KQn+KQn+KQn+KQny5lY2hvMzYwLm9yZ+KQn+KQny8; path=/; domain=.echo360.org;'; }
```

3. **PLAY_SESSION cookie:**

```
Tool: mcp7_browser_evaluate
Parameters:
  function: () => { document.cookie = 'PLAY_SESSION=93b9dd7513db31cc6d6dee032c155a4b8da6dc8a-role=Student&institution=a30bf2d3-ebf0-4b5e-8279-a7e38f3228c3&authn=true&roles=Student&csrfToken=63beb964ea1a4cc034d93808035d520f750aa51a-1760815703535-e1da533513ca4a84a40014bf&sessionExpiresAt=2025-10-18T23%3A28%3A23.514Z&user=833c9952-2b46-4562-b268-f64c26b9db50&sessionCode=42ee4f7d-b23f-4c18-82f7-e8db0212e8ce; path=/; domain=.echo360.org;'; }
```

4. **CloudFront-Key-Pair-Id cookie:**

```
Tool: mcp7_browser_evaluate
Parameters:
  function: () => { document.cookie = 'CloudFront-Key-Pair-Id=APKAIPMYRDQXV3PXG2XA; path=/; domain=.echo360.org;'; }
```

5. **CloudFront-Policy cookie:**

```
Tool: mcp7_browser_evaluate
Parameters:
  function: () => { document.cookie = 'CloudFront-Policy=eyJTdGF0ZW1lbnQiOiBbeyJSZXNvdXJjZSI6Imh0dHBzOi8vKi5lY2hvMzYwLm9yZy8qYTMwYmYyZDMtZWJmMC00YjVlLTgyNzktYTdlMzhmMzIyOGMzLyoiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE3NjA4MjI5MDR9fX1dfQ__; path=/; domain=.echo360.org;'; }
```

6. **CloudFront-Signature cookie:**

```
Tool: mcp7_browser_evaluate
Parameters:
  function: () => { document.cookie = 'CloudFront-Signature=mQu5e9ZetADy-Gvc3HMp8wMt9Fd9fWTvTNFhSCS~OyYo-UIycuxwudQc0eOMOmWEkm9hdQfV1j5AwYEGf-5z4azdFgNREIXO9TM2o9mESuSSHtFaAjGyZk8xJvwqbtzpNWcC~ShX2qSYSSSVlGadEcqQNkKlg90TD0IDIjopOu2psTs2DiZe42sNiLYVj5LVvkwWmbtDn1Baw7Ok4v9xen0dsO4YwJ-akSDKYMXbqHRpoZDFe23n-2JhjQxaQFNgM-6OKtfNSmVciCcYRYOGCGGm1nLbgxYn8cPZMHClkH9axirTplspEPHWcS0mheXsQ9uWQn3k0xmfHmrXDtwVkA__; path=/; domain=.echo360.org;'; }
```

**Step 1.4: Navigate to the Authenticated URL**

After setting ALL cookies, navigate to the content URL again:

```
Tool: mcp7_browser_navigate
Parameters:
  url: https://echo360.org/content#userIdentifier=833c9952-2b46-4562-b268-f64c26b9db50_a30bf2d3-ebf0-4b5e-8279-a7e38f3228c3
```

If successful, you should see:

- Page Title: "Content"
- Page URL: `https://echo360.org/content#userIdentifier=...`
- Navigation menu with "Library", "Courses", "Collections", "Folders"
- A list of media/videos

**COMMON ERRORS:**

1. **Error: "TypeError: result is not a function"**

   - CAUSE: You forgot to wrap the cookie-setting code in `() => { ... }`
   - FIX: Use `() => { document.cookie = '...'; }` NOT `document.cookie = '...'`
2. **Still on login page after navigation**

   - CAUSE: Cookies weren't set correctly or have expired
   - FIX: Verify all 6 cookies were set, or ask user for fresh cookies
3. **Cookies not persisting**

   - CAUSE: Wrong domain or path
   - FIX: Always use `path=/; domain=.echo360.org;` in the cookie string

### 2. How to Go to a Class

**Step 2.1: Navigate to the Courses Page**

From the authenticated library page, click the "Courses" link.

```
Tool: mcp7_browser_click
Parameters:
  element: link "header-user-courses"
  ref: e11
```

This will take you to: `https://echo360.org/courses#userIdentifier=...`

**Step 2.2: Take a Snapshot to See Available Courses**

```
Tool: mcp7_browser_snapshot
```

You will see a grid of courses, typically organized like:

- Fall 2025 - L6133 - 006 - Restricted - Constitutional Law
- Fall 2025 - L6133 - 006 - Published - Constitutional Law
- Fall 2025 - L6105 - 003 - Restricted - Contracts
- etc.

**IMPORTANT:** Lecture recordings are typically in the "Restricted" course, NOT the "Published" course.

**Step 2.3: Click on the Correct Course**

For Constitutional Law (Restricted):

```
Tool: mcp7_browser_click
Parameters:
  element: link "Fall 2025 - L6133 - 006 - Restricted - Constitutional Law"
  ref: e81
```

(Note: The `ref` value will be different each time; use the one from your snapshot)

This takes you to the course home page: `https://echo360.org/section/{section-id}/home`

### 3. How to Find the Right Date

**Step 3.1: View the List of Lectures**

On the course home page, you will see a list of class recordings sorted by date.

```
Tool: mcp7_browser_snapshot
```

The list typically shows:

- September 23, 2025 2:50pm-4:43pm - Constitutional Law
- October 2, 2025 12:00pm-1:43pm - Constitutional Law - Yom Kippur
- October 17, 2025 2:50pm-4:50pm - L6133_006 Make up Session

**Step 3.2: Identify the Most Recent Lecture**

Logic:

1. Use the current date as a reference point
2. Identify the most recent lecture date that has ALREADY PASSED
3. Be aware that lectures listed with future dates are placeholders and will not have content

For example, if today is October 18, 2025, the most recent lecture is "October 17, 2025".

**Step 3.3: Click on the Lecture Link**

```
Tool: mcp7_browser_click
Parameters:
  element: link "Go to class L6133_006 Make up Session October 17, 2025 2:50pm-4:50pm"
  ref: e81
```

(Note: The `ref` value will be different each time; use the one from your snapshot)

This navigates to the lecture video page: `https://echo360.org/lesson/{lesson-id}/classroom`

### 4. How to Download the Transcript

**✅ VERIFIED WORKING METHOD:**

After opening a lecture video page, follow these steps:

**Step 4.1: Open the Transcript Panel**

Click the "transcripts" button in the player controls (bottom right area of the video player):

```
Tool: mcp7_browser_click
Parameters:
  element: button "transcripts"
  ref: [use the ref from your snapshot]
```

This will open the transcript panel on the right side of the screen, showing:
- A search box for searching within the transcript
- The full transcript with speaker labels
- A **"download transcripts"** button at the top

**Step 4.2: Click the Download Button**

```
Tool: mcp7_browser_click
Parameters:
  element: button "download transcripts"
  ref: [use the ref from your snapshot]
```

This will open a download dialog with two format options.

**Step 4.3: Select Download Format**

You'll see two options:
1. **Plain Text Format File (TXT)** - Recommended for readability
2. **VTT Format File** - Video subtitle format with timestamps

For most purposes, choose the Plain Text format:

```
Tool: mcp7_browser_click
Parameters:
  element: button "Plain Text Format File"
  ref: [use the ref from your snapshot]
```

**Step 4.4: File Download Location**

The file will be downloaded to a temporary directory like:
`/var/folders/.../playwright-mcp-output/.../Constitutional-Law-transcript.txt`

The download confirmation will show the exact path in the tool output.

**TRANSCRIPT FORMAT:**

The downloaded TXT file contains:
- Speaker labels (SPEAKER 0, SPEAKER 1, etc.)
- Transcript text organized by speaker
- No timestamps in TXT format (use VTT if you need timestamps)

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
