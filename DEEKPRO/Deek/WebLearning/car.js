let slideIndex = 0;
showSlides(slideIndex);

// Next/previous controls
function moveSlide(n) {
  showSlides(slideIndex += n);
}

function showSlides(n) {
  let slides = document.getElementsByClassName("mySlides");
  
  // Wrap around back to the first slide
  if (n >= slides.length) { 
    slideIndex = 0; 
  }
  // Wrap around back to the last slide
  if (n < 0) { 
    slideIndex = slides.length - 1; 
  }
  
  // Hide all slides
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  
  // Display the active slide
  slides[slideIndex].style.display = "block";  
}
