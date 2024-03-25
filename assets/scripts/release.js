const images = [...document.getElementsByClassName('release-image')];

console.log(images)

const hasImages = images.length > 0;

if (hasImages) {
    const loadingImage = document.querySelector('img.loading');
    const firstImage = images[0];

    console.log(firstImage)

    // set initial image
    loadingImage.src = firstImage.src;
    loadingImage.ref = firstImage.ref;
    loadingImage.classList.remove('loading');

    // create click event
    const imageClickEvent = event => {
        const image = event.target;
        const isSelected = [...image.classList].includes('selected');
    
        if (isSelected) return;
    
        const selectedImage = document.querySelector('img.selected');   
        selectedImage.src = image.src;
        selectedImage.ref = image.ref;
    }
    
    // assign event to images
    images.forEach(image => {
        image.addEventListener('click', imageClickEvent)
    });
}