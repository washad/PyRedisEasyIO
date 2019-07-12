class Keyboard{
    constructor(name, key, value, min, max, allow_decimal, allow_negative, units){
        this.key = key;
        this.original = value;
        this.entry = value;
        this.allow_negative = allow_negative;
        this.allow_decimal = allow_decimal;
        this.min = null;
        this.max = null;
        this._is_decimal_next = false;
        this.first_key = true;

        if (units){
            name = name.concat(' (').concat(units).concat(')')
        }
        $('.easyio_number_keyboard .title').text(name);
        $('.easyio_number_keyboard .original').text(value);

        if (min){
            this.min = Number(min);
            $('.easyio_number_keyboard .min').text(min);
        }
        if (max){
            this.max = Number(max);
            $('.easyio_number_keyboard .max').text(max);
        }

        if (allow_decimal === false){
            $('.easyio_number_keyboard .decimal_button').attr("disabled", true).css('color', 'gray');
        } else{
            $('.easyio_number_keyboard .decimal_button').attr("disabled", false).css('color', 'black');
        }

        if (allow_negative === false){
            $('.easyio_number_keyboard .plus-minus-button').attr("disabled", true).css('color', 'gray');
        } else{
            $('.easyio_number_keyboard .plus-minus-button').attr("disabled", false).css('color', 'black');
        }

        this.clear();

    }

    backspace(){
        if (this.entry === null)        {
            return;
        }
        let s = this.entry.toString();
        if (s.length < 2){
            this.clear();
            return;
        }
        s = s.slice(0, -1);
        this.update(Number(s))
    }

    clear(){
        this.update(null);
        this.first_key = true;
    }


    decimal(){
        if (this.entry === null)        {
            return;
        }
        let s = this.entry.toString();
        if (s.includes('.')){
            return;
        }
        if (this.allow_decimal === false){
            return;
        }
        this._is_decimal_next = true;
    }


    invert_sign(){
        if (this.entry === null)        {
            return;
        }
        if (this.allow_negative === false && this.entry > 0){
            return;
        }
        this.update(this.entry * -1)
    }

    number_pressed(number){
        let s = '';
        if (this.entry === null){
            s = '';
        }
        else{
            s = this.entry.toString();
        }
        if (this.first_key){
            s = '';
            this.first_key = false;
        }
        if (this._is_decimal_next){
            s = s.concat('.');
        }
        s = s.concat(number);
        this._is_decimal_next = false;
        this.update(Number(s))
    }

    show(){
        document.body.classList.add('only-dialog');
        $('.easyio_number_keyboard').show();
    }

    hide(){
        document.body.classList.remove('only-dialog');
        $('.easyio_number_keyboard').hide();
    }

    update(value){
        if (value === null)        {
            document.getElementById('easy_io_number_keyboard_entry').innerText='';
            this.entry = null;
            return;
        }

        let min = this.min;
        let max = this.max;

        if (min && value < min){
            $('.easyio_number_keyboard .min').css('color','red');
            $('.easyio_number_keyboard .ok-button').attr("disabled", true);
            $('.easyio_number_keyboard .ok-button').css('color','gray');
        }
        else if (!(!max) && value > max){
            $('.easyio_number_keyboard .max').css('color','red');
            $('.easyio_number_keyboard .ok-button').attr("disabled", true);
            $('.easyio_number_keyboard .ok-button').css('color','gray');
        }
        else {
            $('.easyio_number_keyboard .ok-button').attr("disabled", false);
            $('.easyio_number_keyboard .ok-button').css('color','blue');
            $('.easyio_number_keyboard .min').css('color','green');
            $('.easyio_number_keyboard .max').css('color','green');
        }

        document.getElementById('easy_io_number_keyboard_entry').innerText = value;
        this.entry = Number(value);
    }

}



let easyio_num_keyboard = null;


function EasyIOChange(event){
    let target = event.currentTarget;
    let name = target.getAttribute('data-name');
    let key = target.getAttribute('data-value-id');
    let units = target.getAttribute('data-units');
    let min = target.getAttribute('data-min');
    let max = target.getAttribute('data-max');
    let allow_decimal=target.getAttribute('data-allow-decimal');
    let allow_negative = target.getAttribute('data-allow-negative');

    let value_element = document.getElementById(key);
    let value = Number(value_element.innerText);
    easyio_num_keyboard = new Keyboard(name, key, value, min, max, allow_decimal, allow_negative, units);
    easyio_num_keyboard.show();
}


function EasyIoNumericEntryKeyPressed(action){
    if (action === 'Del'){
        easyio_num_keyboard.backspace();
    }
    else if (action === 'Clear'){
        easyio_num_keyboard.clear();
    }
    else if (action === 'Cancel'){
        easyio_num_keyboard.hide();
    }
    else if (action === 'Ok'){
        easyio_num_keyboard.hide();
        let id = easyio_num_keyboard.key;
        let value = easyio_num_keyboard.entry;
        let xhttp = new XMLHttpRequest();
        url = `/api/io/${id}/${value}`;
        xhttp.open("POST", url, true);
        xhttp.send();
    }
    else if (action === 'Sign'){
        easyio_num_keyboard.invert_sign();
    }
    else if (action === 'Dec'){
        easyio_num_keyboard.decimal();
    }
    else {
        easyio_num_keyboard.number_pressed(action)
    }
}







