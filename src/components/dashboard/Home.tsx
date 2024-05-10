import { UserModelSchemaType } from "@/schema/UserSchema"
import React, { useEffect, useState } from "react"
import { Button, Container, Paper, Typography } from "@mui/material"
import Link from "next/link"

import dynamic from 'next/dynamic';

const MapContainer = dynamic(() => import('react-leaflet').then((mod) => mod.MapContainer), {
  ssr: false,
});
const TileLayer = dynamic(() => import('react-leaflet').then((mod) => mod.TileLayer), {
  ssr: false,
});
const Marker = dynamic(() => import('react-leaflet').then((mod) => mod.Marker), {
  ssr: false,
});
const Popup = dynamic(() => import('react-leaflet').then((mod) => mod.Popup), {
  ssr: false,
});
const Polyline = dynamic(() => import('react-leaflet').then((mod) => mod.Polyline), {
  ssr: false,
});
import 'leaflet/dist/leaflet.css';

interface IProps {
  user: Omit<UserModelSchemaType, "password">
}

interface SeaLocation {
  name: string
  latitude: number
  longitude: number
}

let userlat = 0;
let userlong = 0;

const nearestSeas: SeaLocation[] = [
  { name: "Black Sea", latitude: 43.3, longitude: 34.0 },
  { name: "Marmara Sea", latitude: 40.7, longitude: 28.0 },
  { name: "Baltic Sea", latitude: 55.0, longitude: 20.0 },
  { name: "Caspian Sea", latitude: 41.6, longitude: 50.6 },
  { name: "North Sea", latitude: 56.0, longitude: 3.0 },
  { name: "Red Sea", latitude: 22.0, longitude: 38.0 },
  { name: "Mediterranean Sea", latitude: 35.0, longitude: 18.0 },
  { name: "Caribbean Sea", latitude: 15.0, longitude: -75.0 },
  { name: "South China Sea", latitude: 12.0, longitude: 112.0 },
  { name: "Coral Sea", latitude: -18.0, longitude: 155.0 },
  { name: "Arabian Sea", latitude: 15.0, longitude: 65.0 },
  { name: "Sea of Okhotsk", latitude: 53.0, longitude: 145.0 },
  { name: "Yellow Sea", latitude: 35.0, longitude: 123.0 },
  { name: "Bering Sea", latitude: 58.0, longitude: -178.0 },
  { name: "Sea of Japan", latitude: 40.0, longitude: 138.0 },
  { name: "Andaman Sea", latitude: 10.0, longitude: 98.0 },
];


const Home = ({ user }: IProps) => {
  const [nearestSea, setNearestSea] = useState<SeaLocation | null>(null)
  const [distance, setDistance] = useState<number | null>(null)
  const [userLocation, setUserLocation] = useState<[number, number] | null>(null);

  useEffect(() => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const userLatitude = position.coords.latitude
          userlat = userLatitude
          const userLongitude = position.coords.longitude
          userlong = userLongitude
          setUserLocation([userLatitude, userLongitude])

          let minDistance = Infinity
          let closestSea: SeaLocation | null = null

          nearestSeas.forEach((sea) => {
            const d = calculateDistance(userLatitude, userLongitude, sea.latitude, sea.longitude)
            if (d < minDistance) {
              minDistance = d
              closestSea = sea
            }
          })

          setNearestSea(closestSea)
          setDistance(minDistance)
        },
        (error) => {
          console.error("Error getting user location:", error)
        }
      )
    }
  }, [])

  const calculateDistance = (lat1: number, lon1: number, lat2: number, lon2: number) => {
    const R = 6371 // Radius of the Earth in kilometers
    const dLat = deg2rad(lat2 - lat1)
    const dLon = deg2rad(lon2 - lon1)
    const a =
      Math.sin(dLat / 2) * Math.sin(dLat / 2) +
      Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) * Math.sin(dLon / 2) * Math.sin(dLon / 2)
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))
    const distance = R * c
    return distance
  }

  const deg2rad = (deg: number) => {
    return deg * (Math.PI / 180)
  }

  return (
    <Paper
      sx={{
        flexGrow: 1,
        py: 5,
        marginTop: 10,
      }}
    >
      <Container maxWidth={false}>
        <Typography variant="h4">Nearest Sea</Typography>
        <Typography variant="caption" gutterBottom>
          based on your location
        </Typography>
        {nearestSea && distance && userLocation && (
          <>
            <Typography variant="body1" marginTop={5}>
              The nearest sea is {nearestSea.name}, approximately {distance.toFixed(2)} kilometers away.
            </Typography>
            <MapContainer
              center={[userLocation[0], userLocation[1]]}
              zoom={4}
              style={{ height: '400px', width: '100%', marginTop: '20px' }}
            >
              <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
              <Polyline
                positions={[
                  [userLocation[0], userLocation[1]],
                  [nearestSea.latitude, nearestSea.longitude],
                ]}
                color="red"
              />
            </MapContainer>
          </>
        )}
      </Container>
    </Paper>
  );
};

export default Home