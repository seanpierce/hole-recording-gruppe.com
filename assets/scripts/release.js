const images = [...document.getElementsByClassName('release-image')];

const hasImages = images.length > 0;

if (hasImages) {
    const loadingImage = document.querySelector('img.loading');
    const firstImage = images[0];

    // set initial image
    loadingImage.src = firstImage.src;
    loadingImage.alt = firstImage.alt;
    loadingImage.classList.remove('loading');

    // create click event
    const imageClickEvent = event => {
        const image = event.target;
        const isSelected = [...image.classList].includes('selected');
    
        if (isSelected) return;
    
        const selectedImage = document.querySelector('img.selected');   
        selectedImage.src = image.src;
        selectedImage.alt = image.alt;
    }
    
    // assign event to images
    images.forEach(image => {
        image.addEventListener('click', imageClickEvent)
    });
}