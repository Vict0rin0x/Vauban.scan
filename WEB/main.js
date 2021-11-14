




function callEelMain(){


    fetchCreate()
}

//Main function to create and put data on the html table
async function fetchCreate() {

    //Python script returns an JSON Object
    //Call with eel of python function
    let obj = await eel.eelMain()()
    //We still need to parse it
    jsonData = JSON.parse(obj)

    //We get the table from html
    let table = document.getElementById('tableJS')
    console.log(jsonData.client_list.length)

    //create an array of row (will be useful later)
    let row = []

    //Loop through JSON returned by python
    for (let element = 0; element < jsonData.client_list.length; element++) {
        //Just a loop to create all rows. Every row is different, they are on row []
        for (let element = 0; element < jsonData.client_list.length; element++) {
            row[element] = table.insertRow();
        }

        //Loop des items dans client list
        //Id + 1 for presentation
        let id = element+1

        //Creation of the cell for id
        let cellId = row[element].insertCell();
        let textId = document.createTextNode(id)
        cellId.appendChild(textId)

        //Creation of the cell for ip address
        let cellIp = row[element].insertCell();
        let textIp = document.createTextNode(jsonData.client_list[element]['ip'])
        cellIp.appendChild(textIp)

        //Creation of the cell for mac address
        let cellMac = row[element].insertCell();
        let textMac = document.createTextNode(jsonData.client_list[element]['mac'])
        cellMac.appendChild(textMac)

        //Creation of the cell for opened ports
        let cellopenports = row[element].insertCell();
        //Loop through client_list.openedPorts[]
        for (let o in jsonData.client_list[element].openPorts) {
            let textOp = document.createTextNode(jsonData.client_list[element].openPorts[o] + " ")
            cellopenports.appendChild(textOp)
        }

        //Creation of the cell for closed ports
        let cellclosedports = row[element].insertCell();
        //Loop de items dans client_list.closedports
        for (let c in jsonData.client_list[element].closedPorts) {
            let textCp = document.createTextNode(jsonData.client_list[element].closedPorts[c] + " ")
            cellclosedports.appendChild(textCp)
        }

        //Creation of the cell for filtered ports
        let cellfilteredports = row[element].insertCell();
        //Loop de items dans client_list.filteredports
        for (let f in jsonData.client_list[element].filteredPorts) {
            let textFp = document.createTextNode(jsonData.client_list[element].filteredPorts[f] + " ")
            cellfilteredports.appendChild(textFp)
        }


        /* For future development
        let services = row[element].insertCell();
        let textServ = document.createTextNode("a faire")
        services.appendChild(textServ)
        */


    }
}


