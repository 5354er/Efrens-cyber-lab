# Vulnerable SQL Injection Lab on Raspberry Pi

This directory contains:
- `search.php`: Vulnerable PHP script running on the Raspberry Pi.
- `sqlmap-findings.txt`: Output from running SQLMap against the vulnerable page.

## Summary

Set up a Raspberry Pi web server with a deliberately vulnerable PHP page using a MySQL database.  
Tested with SQLMap from an Ubuntu VM to identify and exploit a time-based blind SQL injection vulnerability in the `cat` GET parameter.  
The database `testdb` contains a `products` table with sample data that SQLMap was able to extract.

## How to reproduce

1. Deploy `search.php` to a PHP-enabled web server with MySQL backend.  
2. Run SQLMap with:  
   `sqlmap -u "http://<target-ip>/search.php?cat=1" --batch --dump-all`  
3. Review extracted data in the output file.

4. ### Safe SQL Handling Example

`search-safe.php` demonstrates how to securely query a MySQL database using PHP with **prepared statements** (parameterized queries).  
This script safely handles user input (`cat` GET parameter) to prevent SQL injection vulnerabilities that are present in `search.php`.

Key points about `search-safe.php`:
- Uses MySQLi prepared statements to bind parameters securely.
- Prevents attackers from injecting malicious SQL code.
- Properly escapes output using `htmlspecialchars()` to reduce XSS risk.
- Recommended approach for all database-driven PHP applications.

Use `search-safe.php` as a reference for securing vulnerable PHP code in real-world projects.

