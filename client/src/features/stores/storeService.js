const STORES_API = 'https://myduka-api.onrender.com/api/stores'

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

const storeService = {
    getAllStores,
}

export default storeService
