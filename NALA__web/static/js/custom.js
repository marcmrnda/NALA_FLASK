// navigation  menu js
function openNav() {
    $("#myNav").addClass("menu_width");
    $(".menu_btn-style").fadeIn();
}

function closeNav() {
    $("#myNav").removeClass("menu_width");
    $(".menu_btn-style").fadeOut();
}

  // Initialize ScrollReveal
  ScrollReveal().reveal('.reveal', {
    duration: 1000, // Animation duration in milliseconds
    origin: 'bottom', // Animation starting point
    distance: '50px', // Distance the element moves
    easing: 'ease-in-out', // Easing function
    reset: true // Whether the animation should reset when scrolling back up
  });

// get current year

function displayYear() {
    var d = new Date();
    var currentYear = d.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}
displayYear();



//client section owl carousel
$(".owl-carousel").owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    dots: false,
    navText: [
        '<i class="fa fa-long-arrow-left" aria-hidden="true"></i>',
        '<i class="fa fa-long-arrow-right" aria-hidden="true"></i>'
    ],
    autoplay: true,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});


// slider carousel control


$('.slider_btn_prev').on('click', function (e) {
    e.preventDefault()
    $('.slider_text_carousel').carousel('prev')
    $('.slider_image_carousel').carousel('prev')
})


$('.slider_btn_next').on('click', function (e) {
    e.preventDefault()
    $('.slider_text_carousel').carousel('next')
    $('.slider_image_carousel').carousel('next')
})


/** google_map js **/

function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

function translateText() {
    const text = document.getElementById('textToTranslate').value;
    fetch('/translate', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({sentence: text})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('translation').textContent = data.translation;
    })
    .catch(error => console.error('Error:', error));
}

