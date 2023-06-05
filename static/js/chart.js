function keyprosearch(){
    //    XMLHttpRequest is an inbuilt API to establish connection btw server and browser
        var xhttp=new XMLHttpRequest();
        xhttp.open("GET",'/home/contain/'+document.getElementById('keyword').value,true)
        xhttp.onreadystatechange= function(){
            if(this.readyState ==4 && this.status  == 200){
                var data= JSON.parse(this.responseText);
                str= '<table>'
                for(x of data.fd){
                    str=str+'<tr>'
                        str=str+'<td>'+x.id+'<td/>'
                        str=str+'<td>'+x.name+'<td/>'
                        str=str+'<td>'+x.price+'<td/>'
                }
                str=str+'</table>'
                document.getElementById("data").innerHTML=str
            }
        }
        xhttp.send();
    }

function takedrawdata(){
       
            //    XMLHttpRequest is an inbuilt API to establish connection btw server and browser
    var xhttp=new XMLHttpRequest();
    xhttp.open("GET",'/home/jgetda',true)
    xhttp.onreadystatechange= function(){
        if(this.readyState ==4 && this.status  == 200){
            var da= JSON.parse(this.responseText);
            drawchart(da)
        }
    }
    xhttp.send()
}

function drawchart(da){
        
    const myChart = new Chart(
        document.getElementById('myChart'),
        {

            type: 'line',
            data: {
            labels:label(da),
            datasets: [{
                label: 'My chart',
                backgroundColor:'rgb(255,99,132)',
                borderColor:'rgb(255,99,132)',
                data:val(da),
            }]
            },
            options:{}               
            
            }
        );

    }

function label(da){
    let vals=[]
    for(x of da.newval){
        vals.push(x.name)
    }
    return vals
}

function val(da){
    let values=[]
    for(x of da.newval){
        values.push(x.price)
    }
    return values
}