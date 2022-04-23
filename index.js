const getEmployeeList = () => {
    axios.get('http://127.0.0.1:8000/employees')
    .then(function (response) {    
        console.log(response.data)    
        document.getElementById("student-list").innerHTML = JSON.stringify(response.data)

    })
    .catch(function (error) {
        console.log(error);
    });
}

// Load employees when page is loaded
getEmployeeList()

const createEmployee = () => {
    axios.put('http://127.0.0.1:8000/create/employee', {
        name: document.getElementById("name").value,
        position: document.getElementById("profession").value
    })
    .then(function (response) {
        console.log(response);
        document.getElementById("student-list").innerHTML = JSON.stringify(response.data)
    })
    .catch(function (error) {
        console.log(error);
    });
}

const updateEmployee = () => {
    axios.post('http://127.0.0.1:8000/update/employee', {
        employee_id: document.getElementById("id-update").value,
        key: document.getElementById("field").value,
        value: document.getElementById("value").value
    })
    .then(function (response) {
        console.log(response);
        document.getElementById("student-list").innerHTML = JSON.stringify(response.data)
        
    })
    .catch(function (error) {
        console.log(error);
    });
}

const deleteEmployee = () => {
    employee_id = document.getElementById("id-delete").value
    delete_url = 'http://127.0.0.1:8000/delete/employee/' + employee_id
    axios.delete(delete_url)
    .then(function (response) {
        console.log(response);
        document.getElementById("student-list").innerHTML = JSON.stringify(response.data)
    })
    .catch(function (error) {
        console.log(error);
    });
}