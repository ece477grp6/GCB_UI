var map;
var qtWidget;

new QWebChannel(qt.webChannelTransport, function (channel) {
    qtWidget = channel.objects.qtWidget;
});

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 40.450, lng: -86.870},
    zoom: 16
  });
  google.maps.event.addListener(map, 'click', function(event) {
    addMarker(event.latLng);
  });
}

function addMarker(location) {
  var marker = new google.maps.Marker({
    position: location,
    map: map
  });
  var lat = marker.getPosition().lat();
  var lng = marker.getPosition().lng();
  google.maps.event.addListener(marker, 'rightclick', function(event) {
    rmMarker(marker);
  });
  qtWidget.markerAdded(lat, lng);
}

function rmMarker(marker) {
  marker.setMap(null);
  var lat = marker.getPosition().lat();
  var lng = marker.getPosition().lng();
  qtWidget.markerRemoved(lat, lng);
}