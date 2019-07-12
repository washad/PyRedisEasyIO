

function EasyIOSet(event){
    let target = event.currentTarget;
    let id = target.getAttribute('data-value-id');
    let value = target.getAttribute('data-value');
    let xhttp = new XMLHttpRequest();
    url = `/api/io/${id}/${value}`;
    xhttp.open("POST", url, true);
    xhttp.send();
}



$(document).ready(function() {

    function pollPhysicalIO(){
        $.get('/api/io/getall', function(data) {
            let values = JSON.parse(data);

            values.forEach(function(item, index){
                let id = item.id;
                let element = document.getElementById(id);
                if(!(!(element))){
                  element.innerText = item.display_value;
                }
            });
            setTimeout(pollPhysicalIO,500);
        });
    }

    pollPhysicalIO()

});