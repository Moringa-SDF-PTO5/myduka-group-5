const STORES_API = '/api/stores'

//Get all stores
async function getAllStores() {
    try {
        const response = await fetch(STORES_API)
        const responseData = await response.json()

        // console.log('getAllStores called from the Service.')

        return responseData.data
    } catch (error) {
        console.log(error)
    }
}

//Get the count of stores
async function getStoresCount() {
    const response = await fetch(`${STORES_API}/count`)

    const responseData = await response.json()

    return responseData.data
}

const storeService = {
    getAllStores,
    getStoresCount,
}

export default storeService
