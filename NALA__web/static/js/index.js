(function () {
  const win = window;
  const doc = document.documentElement;

  // Update classes to indicate JavaScript is active
  doc.classList.remove('no-js');
  doc.classList.add('js');

  // Reveal animations
  if (document.body.classList.contains('has-animations')) {
    const sr = window.sr = ScrollReveal();
    
    // Set up animations for .feature and .media-canvas elements
    sr.reveal('.feature', {
      duration: 600,
      distance: '20px',
      easing: 'cubic-bezier(0.5, -0.01, 0, 1.005)',
      origin: 'right',
      interval: 100
    });
    sr.reveal('.media-canvas', {
      duration: 600,
      scale: '.95',
      easing: 'cubic-bezier(0.5, -0.01, 0, 1.005)',
      viewFactor: 0.5
    });
  }

  // Device mockup load animation
  const deviceMockup = document.querySelector('.device-mockup');
  if (deviceMockup) {
    const deviceMockupLoaded = () => deviceMockup.classList.add('has-loaded');
    deviceMockup.complete ? deviceMockupLoaded() : deviceMockup.addEventListener('load', deviceMockupLoaded);
  }

  // Adjust features title margin for alignment
  const featuresSection = document.querySelector('.features');
  if (featuresSection) {
    const featuresTitle = featuresSection.querySelector('.section-title');
    const firstFeature = document.querySelector('.feature-inner');

    const updateFeaturesTitlePosition = () => {
      const featuresSectionLeft = featuresSection.querySelector('.features-inner').getBoundingClientRect().left;
      const firstFeatureLeft = firstFeature.getBoundingClientRect().left;
      const offset = firstFeatureLeft > featuresSectionLeft ? firstFeatureLeft - featuresSectionLeft : 0;
      featuresTitle.style.marginLeft = `${offset}px`;
    };

    updateFeaturesTitlePosition();
    win.addEventListener('resize', updateFeaturesTitlePosition);
  }

  // Moving objects effect
  const movingObjects = document.querySelectorAll('.is-moving-object');
  if (movingObjects.length > 0) {
    let mouseX = 0, mouseY = 0, scrollY = 0, winW = doc.clientWidth, winH = doc.clientHeight;

    const moveObjects = (e) => {
      mouseX = e.pageX;
      mouseY = e.pageY;
      scrollY = win.scrollY;
      const coordinateX = (winW / 2) - mouseX;
      const coordinateY = (winH / 2) - (mouseY - scrollY);

      movingObjects.forEach(object => {
        const translatingFactor = object.getAttribute('data-translating-factor') || 20;
        const rotatingFactor = object.getAttribute('data-rotating-factor') || 20;
        const perspective = object.getAttribute('data-perspective') || 500;

        let transformProps = [];
        if (object.classList.contains('is-translating')) {
          transformProps.push(`translate(${coordinateX / translatingFactor}px, ${coordinateY / translatingFactor}px)`);
        }
        if (object.classList.contains('is-rotating')) {
          transformProps.push(`perspective(${perspective}px) rotateY(${-coordinateX / rotatingFactor}deg) rotateX(${coordinateY / rotatingFactor}deg)`);
        }

        if (transformProps.length > 0) {
          object.style.transform = transformProps.join(' ');
          object.style.transition = 'transform 1s ease-out';
          object.style.transformStyle = 'preserve-3d';
          object.style.backfaceVisibility = 'hidden';
        }
      });
    };

    const throttle = (func, limit) => {
      let lastCall = 0;
      return function(...args) {
        const now = Date.now();
        if (now - lastCall >= limit) {
          lastCall = now;
          func.apply(this, args);
        }
      };
    };

    win.addEventListener('mousemove', throttle(moveObjects, 150));
  }
})();


    const playButton = document.querySelector('.media-control');
    const video = document.getElementById('nala-video');

    playButton.addEventListener('click', () => {
        video.style.display = 'block'; // Show the video
        video.style.position = "absolute"
        video.style.top = "0"
        playButton.style.display = 'none'; // Hide the play button
        video.play(); // Start the video
    });
