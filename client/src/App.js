import React, {useState} from 'react'
import axios from 'axios';
import { Icon } from 'leaflet';
import { Alert, Spinner } from 'react-bootstrap';
import { MapContainer, TileLayer, Marker, Popup} from 'react-leaflet';
import useSWR from 'swr';
import "./App.css"

export const icon = new Icon({
    iconUrl: "leaf-green.png",
    shadowUrl: "leaf-shadow.png",
    iconSize: [38, 95],
    shadowSize: [50, 64],
    iconAnchor: [22, 94],
    shadowAnchor: [4, 62],
    popupAnchor: [-3, -76],
 });

const App = () => {
    return (
    <MapContainer center={[53.3498, -6.2603]} zoom = {9}>    
        <TileLayer
            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
         />
    </MapContainer>
    )
}

export default App