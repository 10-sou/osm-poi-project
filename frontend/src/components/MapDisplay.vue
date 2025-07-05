<template>
  <div id="map" style="height: 500px; margin-top: 20px;"></div>
</template>

<script>
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'

export default {
  name: 'MapDisplay',
  props: {
    points: Array
  },
  mounted() {
    this.initMap()
  },
  watch: {
    points: {
      handler() {
        this.updateMarkers()
      },
      deep: true
    }
  },
  methods: {
    initMap() {
      this.map = L.map('map').setView([35.58, 139.56], 13)
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
      }).addTo(this.map)

      this.markerLayer = L.layerGroup().addTo(this.map)
      this.updateMarkers()
    },
    updateMarkers() {
      if (!this.map || !this.markerLayer) return

      this.markerLayer.clearLayers()

      for (const point of this.points) {
        const [lon, lat] = point.coord
        L.circleMarker([lat, lon], {
          radius: 6,
          color: 'red',
          fillColor: '#f03',
          fillOpacity: 0.6
        }).addTo(this.markerLayer).bindPopup(`Mesh ID: ${point.mesh_id}`)
      }

      if (this.points.length > 0) {
        const bounds = this.points.map(p => [p.coord[1], p.coord[0]])
        this.map.fitBounds(bounds)
      }
    }
  }
}
</script>
