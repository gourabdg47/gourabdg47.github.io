---
title: Google Dork Cheat Sheet
author: gourabdg47
date: 25-06-02 11:00:00 +0500
categories:
  - Breach Detected
  - OSINT
tags:
  - reading
  - cybersecurity
  - OSINT
render_with_liquid: false
---
# Google Dorks Cheat Sheet for OSINT Researchers & Investigators

## Basic Search Operators

### Exact Phrase Search

- `"exact phrase"` - Search for exact phrase in quotes
- `"John Smith" AND "New York"` - Find pages containing both exact phrases

### Wildcard and Proximity

- `*` - Wildcard for unknown words
- `AROUND(X)` - Find terms within X words of each other
- `"cyber * attack"` - Find variations like "cyber security attack"

### Boolean Operators

- `AND` / `+` - Both terms must be present
- `OR` / `|` - Either term can be present
- `NOT` / `-` - Exclude specific terms
- `()` - Group terms for complex queries

## Advanced Site-Specific Operators

### Site Targeting

- `site:example.com` - Search within specific domain
- `site:*.gov` - Search all government sites
- `site:linkedin.com "John Smith"` - Find LinkedIn profiles
- `site:reddit.com` - Search Reddit posts and comments

### File Type Searches

- `filetype:pdf` - Find PDF documents
- `filetype:doc` - Find Word documents
- `filetype:xls` - Find Excel spreadsheets
- `filetype:ppt` - Find PowerPoint presentations
- `filetype:txt` - Find text files
- `filetype:log` - Find log files
- `ext:sql` - Alternative syntax for file extensions

### URL Structure Searches

- `inurl:admin` - Find URLs containing "admin"
- `inurl:login` - Find login pages
- `inurl:config` - Find configuration files
- `allinurl:admin panel` - All terms must be in URL

### Title and Text Searches

- `intitle:confidential` - Find pages with "confidential" in title
- `allintitle:secret document` - All terms must be in title
- `intext:password` - Find pages containing "password" in text
- `allintext:classified information` - All terms must be in page text

## OSINT-Specific Techniques

### People Intelligence (PEOPINT)

- `"John Smith" site:linkedin.com` - Find LinkedIn profiles
- `"John Smith" + "email" + "@gmail.com"` - Find email addresses
- `"John Smith" + "phone" + "555"` - Find phone numbers
- `"John Smith" site:facebook.com` - Find Facebook profiles
- `"John Smith" site:twitter.com` - Find Twitter profiles
- `"John Smith" + "resume" filetype:pdf` - Find resumes

### Company Intelligence

- `site:company.com filetype:pdf` - Find company documents
- `"Company Name" + "employee" + "email"` - Find employee emails
- `"Company Name" + "org chart" OR "organizational chart"` - Find org charts
- `"Company Name" + "annual report" filetype:pdf` - Find annual reports
- `site:company.com inurl:careers` - Find job postings

### Location Intelligence (GEOINT)

- `"address" + "city, state" + "zip code"` - Find specific addresses
- `"GPS coordinates" + "latitude longitude"` - Find GPS data
- `site:maps.google.com "location name"` - Find Google Maps data
- `"street view" + "address"` - Find street view images

### Technical Intelligence (TECHINT)

- `site:github.com "company name"` - Find company repositories
- `"API key" + "company name"` - Find exposed API keys
- `"database" + "company name" + "leak"` - Find data breaches
- `"config" + "password" + "database"` - Find configuration files

## Vulnerability and Security Research

### Exposed Files and Directories

- `intitle:"Index of" password` - Find directory listings with passwords
- `intitle:"Index of" "backup"` - Find backup file directories
- `intitle:"Index of" "config"` - Find configuration directories
- `intitle:"Index of" "log"` - Find log file directories

### Login Pages and Admin Panels

- `inurl:admin intitle:login` - Find admin login pages
- `inurl:wp-admin` - Find WordPress admin panels
- `inurl:phpmyadmin` - Find phpMyAdmin interfaces
- `intitle:"admin panel" OR "control panel"` - Find control panels

### Database and System Information

- `intext:"sql syntax near" OR intext:"syntax error has occurred"` - Find SQL errors
- `intext:"Warning: mysql_connect()"` - Find MySQL connection errors
- `intitle:"phpinfo()" "PHP Version"` - Find PHP info pages
- `intext:"Server at" intext:"Apache"` - Find Apache server info

### Credentials and Sensitive Data

- `intext:"username" intext:"password" filetype:log` - Find credentials in logs
- `"password" filetype:txt site:pastebin.com` - Find passwords on Pastebin
- `"BEGIN RSA PRIVATE KEY" filetype:key` - Find private keys
- `"api_key" OR "apikey" filetype:json` - Find API keys in JSON files

## Social Media and Communication

### Social Media Profiles

- `site:linkedin.com/in/ "John Smith"` - LinkedIn profiles
- `site:twitter.com "John Smith"` - Twitter profiles
- `site:facebook.com "John Smith"` - Facebook profiles
- `site:instagram.com "John Smith"` - Instagram profiles

### Forums and Communities

- `site:reddit.com/r/ "topic"` - Search specific subreddits
- `site:stackoverflow.com "company name"` - Find technical discussions
- `"John Smith" site:forum.*` - Find forum posts by person

### Communication Platforms

- `site:discord.com "server name"` - Find Discord servers
- `site:telegram.me "channel name"` - Find Telegram channels
- `"John Smith" + "Skype" + "username"` - Find Skype usernames

## Time-Based and Cache Searches

### Cached and Archived Content

- `cache:example.com` - View Google's cached version
- `site:archive.org "website.com"` - Find archived versions
- `site:web.archive.org "deleted content"` - Find deleted web content

### Date Range Searches

- `after:2023-01-01 before:2023-12-31` - Search within date range
- `"data breach" after:2024-01-01` - Find recent data breaches

## Specialized File and Content Searches

### Documents and Reports

- `"quarterly report" filetype:pdf site:sec.gov` - Find SEC filings
- `"incident report" filetype:pdf "company name"` - Find incident reports
- `"audit report" filetype:pdf` - Find audit documents
- `"meeting minutes" filetype:pdf` - Find meeting records

### Email and Contact Information

- `"@company.com" + "email"` - Find company email addresses
- `intext:"email" + "contact" + "@"` - Find contact emails
- `"john.smith@" + "company.com"` - Find specific email patterns

### Phone Numbers and Addresses

- `"phone" + "555-123-4567"` - Find phone number references
- `"address" + "123 Main Street"` - Find address references
- `"fax" + "company name"` - Find fax numbers

## Advanced Combination Techniques

### Multi-Platform Searches

- `("John Smith" site:linkedin.com) OR ("John Smith" site:twitter.com)` - Search multiple platforms
- `"company name" (site:reddit.com OR site:stackoverflow.com)` - Find discussions across platforms

### Negative Searches for Filtering

- `"John Smith" -site:linkedin.com -site:facebook.com` - Exclude social media
- `"data breach" -news -media` - Exclude news articles
- `"company name" -jobs -careers -hiring` - Exclude job-related content

### Complex Boolean Queries

- `("API key" OR "secret key") AND ("company name") NOT ("example" OR "test")` - Complex credential search
- `(inurl:admin OR inurl:login) AND (intext:password OR intext:username)` - Find admin panels with credentials

## Industry-Specific Searches

### Government and Military

- `site:*.gov "classified" -"declassified"` - Find government classified references
- `site:*.mil "personnel" filetype:pdf` - Find military personnel documents
- `"FOIA" + "document" + "agency name"` - Find FOIA documents

### Healthcare and Medical

- `site:*.edu "patient data" OR "medical records"` - Find healthcare data
- `"HIPAA" + "violation" + "hospital name"` - Find HIPAA violations
- `"clinical trial" + filetype:pdf` - Find clinical trial documents

### Financial and Banking

- `site:sec.gov "10-K" "company name"` - Find SEC 10-K filings
- `"financial statement" filetype:pdf "company name"` - Find financial documents
- `"audit" + "bank" + "report" filetype:pdf` - Find bank audit reports

## Metadata and Hidden Information

### Metadata Searches

- `filetype:pdf "metadata" "author"` - Find PDF metadata
- `"exif data" + "image" + "location"` - Find image metadata
- `"document properties" filetype:doc` - Find Word document properties

### Hidden Text and Comments

- `intext:"hidden" OR intext:"comment"` - Find hidden text
- `"TODO" OR "FIXME" site:github.com` - Find code comments
- `"password" + "comment" filetype:html` - Find passwords in HTML comments

## Best Practices and Tips

### Query Optimization

- Use specific terms rather than generic ones
- Combine multiple operators for precise results
- Use quotes for exact phrases
- Test variations of your queries

### Legal and Ethical Considerations

- Respect robots.txt and terms of service
- Don't access unauthorized systems
- Use information responsibly
- Follow applicable laws and regulations

### Documentation and Verification

- Save search queries and results
- Verify information from multiple sources
- Document the date and time of searches
- Screenshot important findings

## Common Search Patterns

### Identity Verification

```
"John Smith" + "birthday" + "1985"
"John Smith" + "address" + "city"
"John Smith" + "phone" + "email"
```

### Company Research

```
site:company.com filetype:pdf
"company name" + "employee" + "directory"
"company name" + "leak" + "data"
```

### Incident Investigation

```
"incident" + "date" + "location"
"breach" + "company" + "data"
"hack" + "attack" + "victim"
```

### Asset Discovery

```
"company name" + "server" + "IP"
"company name" + "domain" + "subdomain"
"company name" + "network" + "range"
```

This cheat sheet provides a comprehensive foundation for Google Dorking in OSINT investigations. Remember to always operate within legal boundaries and ethical guidelines when conducting research.


> To get in touch with me or for general discussion please visit [ZeroDayMindset Discussion](https://github.com/orgs/X3N0-G0D/discussions/1) 
{: .prompt-info }