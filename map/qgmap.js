var map;
var jshelper;
var poly;
var markers = [];
var currMarker = 0;

new QWebChannel(qt.webChannelTransport, function (channel) {
    jshelper = channel.objects.jshelper;
});

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 40.450, lng: -86.870},
    zoom: 16
  });
  google.maps.event.addListener(map, 'click', function(event) {
    addMarker(event);
  });
  poly = new google.maps.Polyline({
    strokeColor: '#F8C471',
    strokeOpacity: 1.0,
    strokeWeight: 3
  });
  poly.setMap(map);
}

function addMarker(event) {
  var path = poly.getPath();
  path.push(event.latLng);
  // alert(event.latLng);
  var marker = new google.maps.Marker({
    position: event.latLng,
    title: '#' + path.getLength(),
    map: map
  });
  markers.push(marker);
  var markerNum = currMarker + 1;
  currMarker = currMarker + 1;
  google.maps.event.addListener(marker, 'rightclick', function(event) {
    for( currMarker; markerNum <= currMarker; currMarker--){
      rmMarker(markers[currMarker-1]);
      markers.pop();
      path.pop();
    }
  });
  var lat = marker.getPosition().lat();
  var lng = marker.getPosition().lng();
  jshelper.markerAdded(lat, lng);
}

function addMarkerLatlng(latVal, lngVal) {
  var latlng = new google.maps.LatLng({lat: latVal, lng: lngVal}); 
  var path = poly.getPath();
  path.push(latlng);
  var marker = new google.maps.Marker({
    position: latlng,
    title: '#' + path.getLength(),
    map: map
  });
  markers.push(marker);
  var markerNum = currMarker + 1;
  currMarker = currMarker + 1;
  google.maps.event.addListener(marker, 'rightclick', function(event) {
    if(markerNum == currMarker){
      rmMarker(marker);
      markers.pop();
      path.pop();
      currMarker = currMarker -1;
    }
  });
  jshelper.markerAdded(latVal, lngVal);
}

function rmMarker(marker) {
  marker.setMap(null);
  var lat = marker.getPosition().lat();
  var lng = marker.getPosition().lng();
  jshelper.markerRemoved(lat, lng);
}

function clearMarkers() {
  poly.getPath().clear();
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(null);
  }
  jshelper.clearAllMarkers();
}


