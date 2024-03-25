const images = [...document.getElementsByClassName('release-image')];

const imageClickEvent = event => {
    const clickedImage = event.target;
    const isSelected = [...image.classList].includes('selected');

    if (isSelected) return;

    const selectedImage = document.querySelector('img.selected');
    const selectedImageData = {  ...selectedImage };
    const clickedImageData = { ...clickedImage };

    selectedImage.src = clickedImageData.src;
    selectedImage.ref = clickedImageData.ref;
    clickedImage.src = selectedImageData.src;
    clickedImage.ref = selectedImageData.ref;
}

images.forEach(image => {
    image.addEventListener('click', imageClickEvent)
});