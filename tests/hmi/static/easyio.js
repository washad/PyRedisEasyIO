

function EasyIOSet(ns, addr, id){
    let xhttp = new XMLHttpRequest();
    let element = document.getElementById(id);
    url = `/api/io/${id}/true`;
    xhttp.open("POST", url, true);
    xhttp.send();
}

function EasyIOReset(ns, addr, id){
    let xhttp = new XMLHttpRequest();
    let element = document.getElementById(id);
    url = `/api/io/${id}/false`;
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