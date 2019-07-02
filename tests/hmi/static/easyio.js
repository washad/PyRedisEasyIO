

function EasyIOSet(ns, addr, id, value){
    let xhttp = new XMLHttpRequest();
    let element = document.getElementById(id);
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
                  element.innerHTML = item.display_value;
                }
            });
            setTimeout(pollPhysicalIO,500);
        });
    }

    pollPhysicalIO()

});