# OpenSky Network API — Documentação do Projeto

Base URL: `https://opensky-network.org/api`
Autenticação: OAuth2 Bearer Token

---

## CURL 1 — Autenticação

```bash
curl -X POST "https://auth.opensky-network.org/auth/realms/opensky-network/protocol/openid-connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=SEU_CLIENT_ID" \
  -d "client_secret=SEU_CLIENT_SECRET"
```

**Retorno:**
```json
{
  "access_token": "eyJhbGci...",
  "expires_in": 1800
}
```

| Campo | Descrição |
|-------|-----------|
| `access_token` | Token Bearer para usar nas demais chamadas |
| `expires_in` | Tempo em segundos até expirar (1800 = 30 min) |

---

## CURL 2 — Voos em tempo real sobre o Brasil

```bash
curl -H "Authorization: Bearer SEU_TOKEN" \
  "https://opensky-network.org/api/states/all?lamin=-33.7&lamax=5.2&lomin=-73.9&lomax=-34.7"
```

**Parâmetros:**

| Parâmetro | Valor | Descrição |
|-----------|-------|-----------|
| `lamin` | -33.7 | Latitude mínima — sul do Brasil |
| `lamax` | 5.2 | Latitude máxima — norte do Brasil |
| `lomin` | -73.9 | Longitude mínima — oeste do Brasil |
| `lomax` | -34.7 | Longitude máxima — leste do Brasil |

**Retorno — cada voo é um array:**

| Index | Campo | Tipo | Descrição |
|-------|-------|------|-----------|
| 0 | `icao24` | string | Código único da aeronave |
| 1 | `callsign` | string | Número do voo (ex: GLO1234) |
| 2 | `origin_country` | string | País de origem |
| 3 | `time_position` | int | Unix timestamp da última posição |
| 4 | `last_contact` | int | Unix timestamp do último contato |
| 5 | `longitude` | float | Longitude em graus decimais |
| 6 | `latitude` | float | Latitude em graus decimais |
| 7 | `baro_altitude` | float | Altitude barométrica em metros |
| 8 | `on_ground` | bool | Está no solo? |
| 9 | `velocity` | float | Velocidade em m/s |
| 10 | `true_track` | float | Direção em graus (0°=Norte) |
| 11 | `vertical_rate` | float | Subida/descida em m/s |
| 12 | `sensors` | int[] | IDs dos receptores |
| 13 | `geo_altitude` | float | Altitude geométrica em metros |
| 14 | `squawk` | string | Código transponder |
| 15 | `spi` | bool | Indicador especial |
| 16 | `position_source` | int | 0=ADS-B, 1=ASTERIX, 2=MLAT, 3=FLARM |

---

## CURL 3 — Chegadas por aeroporto

```bash
curl -H "Authorization: Bearer SEU_TOKEN" \
  "https://opensky-network.org/api/flights/arrival?airport=SBGR&begin=1517227200&end=1517230800"
```

**Parâmetros:**

| Parâmetro | Descrição |
|-----------|-----------|
| `airport` | Código ICAO do aeroporto (ex: SBGR = Guarulhos) |
| `begin` | Início do período em Unix timestamp |
| `end` | Fim do período em Unix timestamp |

**Retorno:**

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `icao24` | string | Código único da aeronave |
| `callsign` | string | Número do voo |
| `firstSeen` | int | Primeira detecção (Unix) |
| `lastSeen` | int | Última detecção (Unix) |
| `estDepartureAirport` | string | Aeroporto de origem (ICAO) |
| `estArrivalAirport` | string | Aeroporto de destino (ICAO) |
| `estDepartureAirportHorizDistance` | int | Distância horizontal origem (metros) |
| `estDepartureAirportVertDistance` | int | Distância vertical origem (metros) |
| `estArrivalAirportHorizDistance` | int | Distância horizontal destino (metros) |
| `estArrivalAirportVertDistance` | int | Distância vertical destino (metros) |

---

## CURL 4 — Partidas por aeroporto

```bash
curl -H "Authorization: Bearer SEU_TOKEN" \
  "https://opensky-network.org/api/flights/departure?airport=SBGR&begin=1517227200&end=1517230800"
```

**Parâmetros:**

| Parâmetro | Descrição |
|-----------|-----------|
| `airport` | Código ICAO do aeroporto |
| `begin` | Início do período em Unix timestamp |
| `end` | Fim do período em Unix timestamp |

**Retorno:** mesmo formato do CURL 3.

---

## CURL 5 — Voos por intervalo de tempo

```bash
curl -H "Authorization: Bearer SEU_TOKEN" \
  "https://opensky-network.org/api/flights/all?begin=1517227200&end=1517230800"
```

**Parâmetros:**

| Parâmetro | Descrição |
|-----------|-----------|
| `begin` | Início do período em Unix timestamp |
| `end` | Fim do período em Unix timestamp |

**Limite:** intervalo máximo de **2 horas**.

---

## Aeroportos brasileiros principais

| Código ICAO | Aeroporto | Cidade |
|-------------|-----------|--------|
| SBGR | Guarulhos | São Paulo |
| SBGL | Galeão | Rio de Janeiro |
| SBSP | Congonhas | São Paulo |
| SBBR | Brasília | Brasília |
| SBCF | Confins | Belo Horizonte |
| SBPA | Salgado Filho | Porto Alegre |
| SBSV | Deputado Luís Eduardo | Salvador |
| SBRF | Guararapes | Recife |
| SBFZ | Pinto Martins | Fortaleza |
| SBMN | Eduardo Gomes | Manaus |

---

## Conversões úteis

```
velocidade: m/s → km/h       → valor × 3.6
altitude:   metros → pés     → valor × 3.28084
timestamp:  Unix → datetime  → pd.to_datetime(ts, unit='s')

vertical_rate > 0  → subindo
vertical_rate < 0  → descendo
vertical_rate = 0  → nivelado

position_source:
  0 → ADS-B   (mais preciso)
  1 → ASTERIX (radar)
  2 → MLAT    (multilateração)
  3 → FLARM   (aviação geral)
```

---

## Limites de crédito

| Tier | Créditos | Renovação |
|------|----------|-----------|
| Usuário padrão | 4.000 | Diário |
| Feeder ativo | 8.000 | Diário |

| Endpoint | Custo |
|----------|-------|
| `/states/all` Brasil (> 400 sq°) | 4 créditos |
| `/flights/*` | 4 créditos |

**Coleta a cada 10 minutos:**
```
144 chamadas × 4 créditos = 576 créditos/dia
```

---

*Documentação gerada para o projeto pipeline-trafego-aereo — 2026*
