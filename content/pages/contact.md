title: Contact Us
slug: contact
template: page
save_as: contact.html
description: Get in touch with us

# Contact Us

<section>
  <form method="post" action="https://europe-west2-little-bears-416912.cloudfunctions.net/contact-form">
    <p>
      If you would like to visit Little Bears Pre-School, add your child's name
      to our waiting list or would simply like some more information, please
      contact us.
    </p>
    <label>
      First name
      <input name="first_name">
    </label>
    <label>
      Middle name
      <input name="middle_name">
    </label>
    <label>
      Last name
      <input name="last_name">
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
