title: Thank you for contacting us
template: page
slug: contact
save_as: contact-success.html

# Contact Us

<section>
  <form>
    <p>
      Thank you for contacting us.
    </p>
    <p>
      We will get back to you as soon as possible.
    </p>
  </form>
  <div class="map-wrapper"><div id="map"></div></div>
</section>

<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
        integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
        crossorigin=""></script>
<script>
var map = L.map('map').setView([51.68375413584007, -1.1303268653223957], 16);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 19,
  attribution: '&copy; OpenStreetMap'
}).addTo(map);
L.marker([51.68375413584007, -1.1303268653223957]).addTo(map);
</script>
