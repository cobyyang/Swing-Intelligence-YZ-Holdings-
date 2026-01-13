# Security Hardening & WAF Configuration

This document outlines the security measures implemented for the Swing Intelligence platform (Production Grade).

## 1. WAF & Edge Protection (Cloudflare Recommended)

Before traffic hits the application, it should be filtered by an Edge WAF (Cloudflare).

### A. Bot Fight Mode
*   **Action:** Enable "Bot Fight Mode" or "Super Bot Fight Mode".
*   **Rule:** Block known bad bots. Challenge likely automated traffic.

### B. WAF Custom Rules (Firewall Rules)

Create the following rules in Cloudflare WAF:

1.  **Rate Limit Login Endpoints**
    *   **URI Path:** `contains` `/api/auth/`
    *   **Action:** Rate Limit (Cloudflare Rate Limiting)
    *   **Threshold:** 5 requests per 1 minute per IP.
    *   **Block Duration:** 1 hour.

2.  **Protect Expensive Endpoints (Thesis Generation)**
    *   **URI Path:** `contains` `/api/thesis/generate`
    *   **Action:** Rate Limit
    *   **Threshold:** 3 requests per 1 minute per IP.
    *   **Block Duration:** 1 hour.

3.  **Block Bad User Agents**
    *   **User Agent:** `contains` `python-requests`, `curl`, `wget`, `go-http-client` (unless explicitly allowed for internal tools).
    *   **Action:** Block.

4.  **Geo-Blocking (Optional)**
    *   **Country:** `not in` {Target Markets e.g., US, CA, UK, EU}
    *   **Action:** Managed Challenge.

## 2. Application Security (Backend Hardening)

The backend (`api/`) is hardened with the following layers:

### A. Middleware Stack
1.  **Request Context:** Assigns a unique `X-Request-ID` to every request for tracing.
2.  **Helmet (CSP & Headers):**
    *   `Content-Security-Policy`: Strict default.
    *   `X-Frame-Options`: DENY (Prevents Clickjacking).
    *   `X-Content-Type-Options`: nosniff.
    *   `Strict-Transport-Security`: Enabled in production.
3.  **CORS:** Strict allowlist. Only allows `APP_ORIGIN` (Production) or `localhost` (Dev).
4.  **Rate Limiting (Server-side fallback):**
    *   Global: 120 req/min.
    *   Auth: 5 req/min.
    *   Thesis: 3 req/min.
    *   Movers Refresh: 2 req/min.
5.  **Authentication (`authRequired`):**
    *   Enforced on all `/api/*` routes except explicit allowlist (`/health`, `/market/ticker` public data).
    *   Populates `req.user`.
    *   **IDOR Protection:** Routes MUST use `req.user.id` and IGNORE client-provided `userId`.
6.  **Input Validation (Zod):**
    *   All write/sensitive endpoints validate `body`, `query`, and `params` using strict Zod schemas.
    *   Unknown fields are rejected.

### B. Secrets Management
*   **Startup Check:** Server refuses to start if critical env vars (`SUPABASE_SERVICE_ROLE_KEY`, `OPENAI_API_KEY`) are missing.
*   **Leak Prevention:** `SUPABASE_SERVICE_ROLE_KEY` is NEVER exposed to the frontend.

## 3. Frontend Security

1.  **Safe API Fetching:**
    *   `apiFetch` utility handles auth tokens automatically.
    *   **401 Handling:** Auto-redirects to login on session expiry.
    *   **No Logging:** Tokens are never logged to console.
2.  **XSS Protection:**
    *   React's default escaping is relied upon.
    *   `dangerouslySetInnerHTML` is strictly avoided.

## 4. Verification & Incident Response

### Verification Commands

**1. Test Unauthorized Access (Should return 401)**
```bash
curl -I -X POST http://localhost:3001/api/watchlist -d '{"symbol":"AAPL"}'
# Expect: HTTP/1.1 401 Unauthorized
```

**2. Test Rate Limiting (Spam request)**
```bash
# Run 10 times quickly
for i in {1..10}; do curl -I http://localhost:3001/api/auth/login; done
# Expect: 429 Too Many Requests after threshold
```

**3. Test Validation (Bad Payload)**
```bash
curl -X POST http://localhost:3001/api/watchlist \
  -H "Authorization: Bearer <VALID_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"symbol":"INVALID_SYMBOL_TOO_LONG"}'
# Expect: 400 Bad Request (Validation Error)
```

**4. Test CORS (Bad Origin)**
```bash
curl -I -H "Origin: http://evil.com" http://localhost:3001/api/health
# Expect: CORS error (missing Access-Control-Allow-Origin header)
```

### Incident Response Plan

1.  **Leak Detected:**
    *   Rotate `SUPABASE_SERVICE_ROLE_KEY` in Supabase Dashboard immediately.
    *   Update `.env` on server and redeploy.
    *   Invalidate all user sessions (`auth.sessions` truncation if necessary).

2.  **DDoS Attack:**
    *   Enable "Under Attack Mode" in Cloudflare.
    *   Review `api` logs for specific IP patterns and block in WAF.

3.  **Data Breach:**
    *   Disable API access (Stop server).
    *   Audit logs using `requestId` to identify scope.
