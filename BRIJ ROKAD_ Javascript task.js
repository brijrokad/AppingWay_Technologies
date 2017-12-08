var data =  [0,1,2,"stop",2,0,1,"stop"];

function remove(array,element){ 
        for(var i = array.length-1; i--;){
                if(array[i] === element) // It will check the entire array
                    array.splice(i, 1); // If zero found it will remove it 
        }                               // splice is pre-define function
}

remove(data,0) // function call
console.log(data.toString());