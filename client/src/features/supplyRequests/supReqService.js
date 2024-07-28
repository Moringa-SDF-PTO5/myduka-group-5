const SUPPLY_REQUEST_URL = '/api/supply_requests'

//Add a supply request to the db
async function addSupplyRequest(supReqData) {
    const response = await fetch(SUPPLY_REQUEST_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(supReqData),
    })

    const responseData = await response.json()

    if (responseData.status === 'error') {
        throw new Error(responseData.message)
    }

    return responseData.data
}

//Get all supply requests
async function getAllSupplyRequests() {
    const response = await fetch(SUPPLY_REQUEST_URL)

    const responseData = await response.json()

    return responseData.data
}

//Edit one supply request
async function editSupplyRequest(id, supReqData) {
    const response = await fetch(`${SUPPLY_REQUEST_URL}/${id}`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(supReqData),
    })

    const responseData = await response.json()

    if (responseData.data === null) {
        throw new Error(responseData.message)
    }

    return responseData.data
}

const supReqService = {
    addSupplyRequest,
    getAllSupplyRequests,
    editSupplyRequest,
}

export default supReqService
