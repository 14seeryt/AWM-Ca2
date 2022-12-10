import React from 'react'
import { MapContainer, TileLayer} from 'react-leaflet';
import { L } from 'leaflet';
import "./App.css"

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