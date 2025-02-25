function initAutocomplete() {
  var input = document.getElementById('location-input');
  var autocomplete = new google.maps.places.Autocomplete(input);
  var searchButton = document.getElementById("search-btn");
  input.addEventListener('input', function () {
    searchButton.disabled = true;
  });

  autocomplete.addListener('place_changed', function() {
    var place = autocomplete.getPlace();
    if (place.geometry) {
      searchButton.disabled = false;
    }
  });
}