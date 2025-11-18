# Security Policy

## Supported Versions
Security updates are provided for the latest stable release of this platform.

## Reporting a Vulnerability
If you discover a security issue:
- Email: security@company.com
- Telegram: @SecurityOpsBot

We respond within 24 hours.

Do NOT publicly disclose vulnerabilities before contacting us.

## System Security Overview
- Web Application Firewall (WAF)
- Fail2Ban with custom jails
- Nginx rate-limiting and hardening
- Enforced HTTPS (TLS 1.3)
- Input sanitization on all API endpoints
- JWT-based authentication
- Password hashing using bcrypt with salt
- Suspicious activity tracking via AI (security_ai.py)
- Self-healing AI modules that detect, patch, and quarantine threats automatically

## Password Policy
- Min length: 10 chars
- Must include: lowercase, uppercase, number, symbol

## Data Protection
- AES-256 encryption for sensitive fields
- Database at-rest encryption enabled
- Secure backups rotated every 24h
