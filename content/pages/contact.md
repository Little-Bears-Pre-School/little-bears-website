title: Contact Us
slug: contact
template: page
save_as: contact.html
description: Get in touch with us

# Contact Us

<section>
  <form method="post" action="https://europe-west2-little-bears-429116.cloudfunctions.net/contact-form">
    <p>
      If you would like to visit Little Bears Pre-School, add your child's name
      to our waiting list or would simply like some more information, please
      contact us.
    </p>
    <p class="alert">
      We are currently fully subscribed for 2024-2025, and have a full waiting list. You can
      still apply for a place from September 2025 onwards.
    </p>
    <label>
      Title
      <input name="title">
    </label>
    <label>
      Full name
      <input name="full_name">
    </label>
    <label>
      Email address
      <input type="email" name="email">
    </label>
    <label>
      Phone number
      <input type="phone" name="phone">
    </label>
    <label>
      Message
      <textarea name="message"></textarea>
    </label>
    <button>Send</button>
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
