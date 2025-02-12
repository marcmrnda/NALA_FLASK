 // Initialize ScrollReveal
  ScrollReveal().reveal('.reveal', {
    duration: 1000, // Animation duration in milliseconds
    origin: 'bottom', // Animation starting point
    distance: '50px', // Distance the element moves
    easing: 'ease-in-out', // Easing function
    reset: true // Whether the animation should reset when scrolling back up
  });


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
    const mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    const map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}



const swapBtn = document.querySelector(".swap-position"),
  inputChars = document.getElementById('input-chars'),
  inputTextElem = document.getElementById("input-text"),
  outputTextElem = document.getElementById("output-text"),
  inputLangSelect = document.getElementById("input-language"),
  outputLangSelect = document.getElementById("output-language");

  inputTextElem.addEventListener("input", (e) => {
    e.preventDefault()
    inputChars.textContent = inputTextElem.value.length
    //limit input to 5000 characters
    if (inputTextElem.value.length > 5000) {
      inputTextElem.value = inputTextElem.value.slice(0, 5000);
    }
  });

// Swap function
swapBtn.addEventListener("click", () => {
  // Swap language selections
  const tempLang =  inputLangSelect.options[inputLangSelect.selectedIndex].textContent;
  inputLangSelect.options[inputLangSelect.selectedIndex].textContent = outputLangSelect.options[outputLangSelect.selectedIndex].textContent;
  outputLangSelect.options[outputLangSelect.selectedIndex].textContent = tempLang;

  const tempValue = inputLangSelect.options[inputLangSelect.selectedIndex].value.replace("_to_", "")
  const tempValue2 = outputLangSelect.options[outputLangSelect.selectedIndex].value.padEnd(7,"_to_")
  inputLangSelect.options[inputLangSelect.selectedIndex].value = tempValue2
  outputLangSelect.options[outputLangSelect.selectedIndex].value = tempValue;


  console.log(outputLangSelect.options[outputLangSelect.selectedIndex],inputLangSelect.options[inputLangSelect.selectedIndex])

  // Swap text areas
  const tempText = inputTextElem.value;
  inputTextElem.value = outputTextElem.value;
  outputTextElem.value = tempText;
});


