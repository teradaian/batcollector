let parent = document.querySelector('#parent');
let colorPicker = document.querySelector('#id_color')

let picker = new Picker(parent);

picker.onChange = function(color) {
    colorPicker.value = color.rgbaString;
};

colorPicker.addEventListener("click", (evt) => {
    picker.open()
})

