# Phase 1: Live Space Weather Data - Complete Context

## Overview
Phase 1 is a **real-time space weather monitoring dashboard** that displays live data from multiple sources with scientist-grade analysis and visualization.

## Frontend Architecture

### Main Component: `Phase1.tsx`
- **Location**: `frontend/src/pages/Phase1.tsx`
- **Purpose**: Real-time space weather data visualization and analysis
- **Layout**: 4-grid responsive layout (2x2 on desktop, stacked on mobile)

### Key Features

1. **Parameter Selection System**
   - 15+ space weather parameters
   - Manual navigation (Previous/Next buttons)
   - Parameter selector bar at bottom
   - Each parameter has detailed info, graphs, animations, and effects

2. **Parameters Displayed**:
   - Kp Index (Planetary K-index)
   - DST Index (Disturbance Storm Time)
   - Solar Wind Speed
   - Solar Wind Density
   - Bz Component (IMF Bz GSM)
   - Bt (Total IMF Magnitude)
   - Bx Component (IMF Bx GSM)
   - By Component (IMF By GSM)
   - Wind Longitude (GSM)
   - Wind Latitude (GSM)
   - Solar Wind Temperature
   - F10.7 Flux
   - Kp Forecast
   - Ap Index
   - Sun Activity (Aditya L1 instruments)

3. **4-Grid Layout** (for each parameter):
   - **Grid 1**: Parameter Info Card
     - Current value with color coding
     - Range, average, limits
     - Definition and technical details
     - Navigation buttons
   
   - **Grid 2**: Real-time Graph
     - Line chart showing last 24 hours
     - Uses Recharts library
     - Color-coded by parameter
   
   - **Grid 3**: 3D Visualization/Animations
     - Parameter-specific animations
     - Uses `ParameterSpecificAnimation` component
     - Different animation types: particle, geomagnetic, field, image
   
   - **Grid 4**: Effects & Safety Analysis
     - Dynamic effects based on current value
     - Safe/Not Safe conditions
     - Scientific analysis
     - Status badges (Safe/Warning/Danger)

4. **Special Layout for "Sun Activity"**:
   - Shows Aditya L1 instrument information
   - Coronagraph images (LASCO C3)
   - EUV Imager images (SUVI 094)
   - Flare Monitor data
   - Image carousel with animations

### Data Fetching

Phase 1 fetches data from these API endpoints:

```typescript
// All data fetched in parallel using Promise.allSettled
const [realtime, geomagnetic, alerts, flares, lasco, suvi] = await Promise.allSettled([
  api.getRealtimeData(),                    // /api/data/realtime
  api.getLiveGeomagneticStorm(),            // /api/geomagnetic/storm/live
  api.getSpaceWeatherAlerts(),              // /api/noaa/alerts
  api.getSolarFlaresData(),                  // /api/noaa/solar-flares
  api.getImageSequenceForGif('lasco-c3', 5), // /api/noaa/images/lasco-c3
  api.getImageSequenceForGif('suvi-094', 5)  // /api/noaa/images/suvi-094
]);
```

**Refresh Interval**: Every 60 seconds (1 minute)

### Helper Functions: `Phase1Helpers.ts`

**Purpose**: Dynamic parameter analysis based on current values

**Key Function**: `getDynamicParameterInfo(param: ParameterData)`

This function provides:
- **Dynamic Effects**: Based on current value thresholds
- **Safe Conditions**: When values are normal
- **Not Safe Conditions**: When precautions are needed
- **Status**: 'safe' | 'warning' | 'danger'
- **Status Message**: Human-readable status
- **Scientific Details**: Technical analysis

**Example Logic**:
- Kp >= 7: SEVERE storm, power grid disruptions, satellite risks
- DST <= -100: Severe geomagnetic storm
- Speed >= 900 km/s: EXTREME high-speed stream
- Bz <= -15 nT: STRONG southward field, major storm likely

## Backend API Endpoints

### 1. `/api/data/realtime` (GET)
**Purpose**: Get real-time solar wind data

**Implementation**: `backend/main.py` line 1055

**Data Source**: NOAA Combined Real-time Data (`noaa_realtime_data.get_combined_realtime_data()`)

**Returns**:
```json
{
  "success": true,
  "data_source": "NOAA Combined",
  "timestamp": "2025-01-XX...",
  "solar_wind": {
    "speed": 450.0,
    "velocity": 450.0,
    "density": 5.2,
    "temperature": 105000,
    "bx_gsm": 2.1,
    "by_gsm": -1.5,
    "bz_gsm": -3.2,
    "bt": 4.5,
    "lon_gsm": 5.0,
    "lat_gsm": -2.0
  },
  "speed": 450.0,
  "density": 5.2,
  "temperature": 105000,
  "bz": -3.2,
  "bt": 4.5,
  "lon": 5.0,
  "lat": -2.0,
  "history": {
    "timestamps": ["2025-01-XX..."],
    "speed": [450.0, 455.0, ...],
    "density": [5.2, 5.5, ...],
    "temperature": [105000, 106000, ...]
  },
  "cme_events": [],
  "message": "Real-time combined telemetry"
}
```

**Fallback**: If NOAA fails, returns synthetic data

---

### 2. `/api/geomagnetic/storm/live` (GET)
**Purpose**: Get live geomagnetic indices (Kp, DST, F10.7, Ap)

**Implementation**: `backend/main.py` line 4493

**Data Sources**:
- `get_dst_index()` - DST index
- `get_kp_index()` - Kp index
- `get_f107_flux()` - F10.7 solar flux
- `get_kp_forecast()` - Kp forecast

**Returns**:
```json
{
  "success": true,
  "indices": {
    "Dst": -15.0,
    "Kp": 3.5,
    "Ap": 12.0,
    "F10.7": 125.5
  },
  "kp_forecast": 4.0,
  "forecast": {
    "Kp": 4.0
  },
  "timeline": [
    {
      "timestamp": "2025-01-XX...",
      "Dst": -15.0,
      "Kp": 3.5
    }
  ],
  "dst_data": {...},
  "kp_data": {...},
  "f107_data": {...},
  "last_update": "2025-01-XX..."
}
```

---

### 3. `/api/noaa/alerts` (GET)
**Purpose**: Get space weather alerts from NOAA

**Implementation**: `backend/main.py` line 4461

**Data Source**: `noaa_realtime_data.get_space_weather_alerts()`

**Returns**:
```json
{
  "success": true,
  "data": [
    {
      "message": "Geomagnetic Storm Warning",
      "issue_datetime": "2025-01-XX...",
      "description": "..."
    }
  ],
  "total_alerts": 2
}
```

**Frontend Usage**: Shows alerts as toast notifications (max 3)

---

### 4. `/api/noaa/solar-flares` (GET)
**Purpose**: Get solar flare data

**Implementation**: `backend/main.py` line 4477

**Data Source**: `noaa_realtime_data.get_solar_flares_data()`

**Returns**:
```json
{
  "success": true,
  "data": [
    {
      "class": "M2.5",
      "begin_time": "2025-01-XX...",
      "peak_time": "2025-01-XX...",
      "end_time": "2025-01-XX...",
      "source_location": "N15W45",
      "region": "AR12345"
    }
  ]
}
```

---

### 5. `/api/noaa/images/{source}` (GET)
**Purpose**: Get image sequences for animations

**Implementation**: `backend/main.py` line 4425

**Parameters**:
- `source`: `lasco-c3`, `lasco-c2`, `suvi-094`, `enlil`, `ovation-north`, `ovation-south`
- `count`: Number of images (default: 1)

**Data Source**: `noaa_realtime_data.get_image_sequence_for_gif(source, count)`

**Returns**:
```json
{
  "success": true,
  "data": [
    "https://services.swpc.noaa.gov/.../image1.jpg",
    "https://services.swpc.noaa.gov/.../image2.jpg"
  ],
  "images": [...],
  "gifs": {
    "movie_24h": "https://.../movie_24h.gif",
    "movie_7d": "https://.../movie_7d.gif"
  }
}
```

**Frontend Usage**: 
- LASCO C3: Coronagraph images for CME detection
- SUVI 094: EUV images for active region monitoring

## Data Flow

```
Phase1 Component
    ↓
Fetch All Data (Promise.allSettled)
    ├─→ /api/data/realtime → NOAA Combined Data
    ├─→ /api/geomagnetic/storm/live → Kp, DST, F10.7
    ├─→ /api/noaa/alerts → Space Weather Alerts
    ├─→ /api/noaa/solar-flares → Solar Flare Data
    ├─→ /api/noaa/images/lasco-c3 → Coronagraph Images
    └─→ /api/noaa/images/suvi-094 → EUV Images
    ↓
Update State
    ↓
Render 4-Grid Layout
    ├─→ Parameter Info (with dynamic analysis)
    ├─→ Real-time Graph (Recharts)
    ├─→ 3D Animation (ParameterSpecificAnimation)
    └─→ Effects & Safety (getDynamicParameterInfo)
    ↓
Auto-refresh every 60 seconds
```

## Key Components Used

1. **ParameterSpecificAnimation**: 3D visualizations based on parameter type
2. **ImageCarousel**: Cycles through images for animations
3. **Recharts**: Line charts for time series data
4. **Framer Motion**: Animations and transitions
5. **Sonner Toast**: Alert notifications

## Data Sources (NOAA)

All data comes from **NOAA Space Weather Prediction Center**:
- **FREE** - No API key needed
- **REAL-TIME** - Updates every minute
- **RELIABLE** - US government data
- **NO RATE LIMITS**

**Base URLs**:
- Solar Wind: `https://services.swpc.noaa.gov/products/solar-wind/`
- Geomagnetic: `https://services.swpc.noaa.gov/products/geospace/`
- Images: `https://services.swpc.noaa.gov/products/animations/`
- Alerts: `https://services.swpc.noaa.gov/products/alerts/`

## Special Features

1. **Dynamic Analysis**: Effects and safety recommendations change based on current values
2. **Scientist-Grade Details**: Technical analysis for each parameter
3. **Real-time Updates**: Auto-refresh every minute
4. **Alert System**: Toast notifications for space weather alerts
5. **Image Animations**: GIFs and image carousels for visual data
6. **Parameter Navigation**: Easy switching between parameters

## Error Handling

- All API calls use `Promise.allSettled` to prevent one failure from breaking others
- Fallback synthetic data if NOAA fails
- Graceful degradation with loading states
- Error messages in console, user-friendly messages in UI

## Performance

- **Parallel Data Fetching**: All APIs called simultaneously
- **60-second Refresh**: Balanced between real-time and server load
- **Efficient Re-renders**: React state management
- **Image Lazy Loading**: Images load on demand

## Future Enhancements

- WebSocket for real-time streaming
- Historical data comparison
- Export data functionality
- Custom parameter combinations
- Alert threshold configuration







