-- =============================================
-- CAMADA BRONZE — Dados brutos da API OpenSky
-- =============================================

-- Voos em tempo real sobre o Brasil
CREATE TABLE IF NOT EXISTS raw_voos (
    id              SERIAL PRIMARY KEY,
    icao24          VARCHAR(10),
    callsign        VARCHAR(20),
    origin_country  VARCHAR(100),
    time_position   BIGINT,
    last_contact    BIGINT,
    longitude       DECIMAL(10, 6),
    latitude        DECIMAL(10, 6),
    baro_altitude   DECIMAL(10, 2),
    on_ground       BOOLEAN,
    velocity        DECIMAL(10, 2),
    true_track      DECIMAL(10, 2),
    vertical_rate   DECIMAL(10, 2),
    sensors         TEXT,
    geo_altitude    DECIMAL(10, 2),
    squawk          VARCHAR(10),
    spi             BOOLEAN,
    position_source SMALLINT,
    coletado_em     TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS raw_chegadas (
    id                                 SERIAL PRIMARY KEY,
    icao24                             VARCHAR(10),
    first_seen                         BIGINT,
    est_departure_airport              VARCHAR(10),
    last_seen                          BIGINT,
    est_arrival_airport                VARCHAR(10),
    callsign                           VARCHAR(20),
    est_departure_airport_horiz_dist   INT,
    est_departure_airport_vert_dist    INT,
    est_arrival_airport_horiz_dist     INT,
    est_arrival_airport_vert_dist      INT,
    departure_airport_candidates_count INT,
    arrival_airport_candidates_count   INT,
    coletado_em                        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS raw_partidas (
    id                                 SERIAL PRIMARY KEY,
    icao24                             VARCHAR(10),
    first_seen                         BIGINT,
    est_departure_airport              VARCHAR(10),
    last_seen                          BIGINT,
    est_arrival_airport                VARCHAR(10),
    callsign                           VARCHAR(20),
    est_departure_airport_horiz_dist   INT,
    est_departure_airport_vert_dist    INT,
    est_arrival_airport_horiz_dist     INT,
    est_arrival_airport_vert_dist      INT,
    departure_airport_candidates_count INT,
    arrival_airport_candidates_count   INT,
    coletado_em                        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS raw_intervalo (
    id                                 SERIAL PRIMARY KEY,
    icao24                             VARCHAR(10),
    first_seen                         BIGINT,
    est_departure_airport              VARCHAR(10),
    last_seen                          BIGINT,
    est_arrival_airport                VARCHAR(10),
    callsign                           VARCHAR(20),
    est_departure_airport_horiz_dist   INT,
    est_departure_airport_vert_dist    INT,
    est_arrival_airport_horiz_dist     INT,
    est_arrival_airport_vert_dist      INT,
    departure_airport_candidates_count INT,
    arrival_airport_candidates_count   INT,
    coletado_em                        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);