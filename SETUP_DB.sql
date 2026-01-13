
-- 1. Master Tickers Table
CREATE TABLE IF NOT EXISTS tickers (
    symbol TEXT PRIMARY KEY,
    name TEXT,
    exchange TEXT,
    sector TEXT,
    industry TEXT,
    type TEXT, -- 'stock', 'etf'
    is_active BOOLEAN DEFAULT true,
    is_us BOOLEAN DEFAULT true,
    created_at TIMESTAMPTZ DEFAULT now()
);

-- 1.1 Universe Membership
CREATE TABLE IF NOT EXISTS ticker_universes (
    universe TEXT, -- 'ALL_US', 'SP500', 'NASDAQ100', 'RUSSELL2000'
    symbol TEXT REFERENCES tickers(symbol) ON DELETE CASCADE,
    PRIMARY KEY (universe, symbol)
);

-- 2. Ticker Snapshot (Real-time Price + Basic Stats)
CREATE TABLE IF NOT EXISTS ticker_snapshot (
    symbol TEXT PRIMARY KEY REFERENCES tickers(symbol) ON DELETE CASCADE,
    price NUMERIC,
    change NUMERIC,
    percent_change NUMERIC,
    volume BIGINT,
    previous_close NUMERIC,
    open NUMERIC,
    high NUMERIC,
    low NUMERIC,
    market_cap NUMERIC, -- Added
    high_52w NUMERIC,   -- Added
    low_52w NUMERIC,    -- Added
    updated_at TIMESTAMPTZ DEFAULT now()
);

-- 3. Ticker Indicators (Technical Analysis)
CREATE TABLE IF NOT EXISTS ticker_indicators (
    symbol TEXT PRIMARY KEY REFERENCES tickers(symbol) ON DELETE CASCADE,
    rsi14 NUMERIC,
    sma50 NUMERIC,
    sma200 NUMERIC,
    atr14 NUMERIC,
    atr_percent NUMERIC,
    updated_at TIMESTAMPTZ DEFAULT now()
);

-- 3.5 Screener Cache (Fast Read Table)
-- This effectively joins the above for the "Market Movers" view
CREATE TABLE IF NOT EXISTS screener_cache_daily (
    symbol TEXT PRIMARY KEY REFERENCES tickers(symbol) ON DELETE CASCADE,
    price NUMERIC,
    percent_change NUMERIC,
    market_cap NUMERIC,
    volume BIGINT,
    rsi14 NUMERIC,
    sma50_state TEXT, -- 'above', 'below'
    atr_percent NUMERIC,
    updated_at TIMESTAMPTZ DEFAULT now()
);

-- 4. Job Runs (Queue)
CREATE TABLE IF NOT EXISTS job_runs (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    job_name TEXT,
    status TEXT DEFAULT 'queued',
    metadata JSONB,
    started_at TIMESTAMPTZ DEFAULT now(),
    finished_at TIMESTAMPTZ,
    processed_count INT,
    error TEXT
);

-- Indexes for Performance
CREATE INDEX IF NOT EXISTS idx_tickers_sector ON tickers(sector);
CREATE INDEX IF NOT EXISTS idx_universe_lookup ON ticker_universes(universe);
CREATE INDEX IF NOT EXISTS idx_screener_change ON screener_cache_daily(percent_change);
CREATE INDEX IF NOT EXISTS idx_screener_mcap ON screener_cache_daily(market_cap);
CREATE INDEX IF NOT EXISTS idx_screener_volume ON screener_cache_daily(volume);

-- Views (Optional helper)
CREATE OR REPLACE VIEW market_movers_view AS
SELECT 
    t.symbol, t.name, t.sector,
    s.price, s.percent_change, s.market_cap, s.volume,
    s.high_52w, s.low_52w,
    i.rsi14, i.atr_percent,
    CASE WHEN s.price > i.sma50 THEN 'above' ELSE 'below' END as sma50_state
FROM tickers t
LEFT JOIN ticker_snapshot s ON t.symbol = s.symbol
LEFT JOIN ticker_indicators i ON t.symbol = i.symbol
WHERE t.is_active = true;

-- Enable RLS
ALTER TABLE tickers ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Public Read Tickers" ON tickers FOR SELECT USING (true);
ALTER TABLE ticker_snapshot ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Public Read Snapshots" ON ticker_snapshot FOR SELECT USING (true);
ALTER TABLE ticker_indicators ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Public Read Indicators" ON ticker_indicators FOR SELECT USING (true);
ALTER TABLE ticker_universes ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Public Read Universes" ON ticker_universes FOR SELECT USING (true);
ALTER TABLE screener_cache_daily ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Public Read Screener" ON screener_cache_daily FOR SELECT USING (true);
